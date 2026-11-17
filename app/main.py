from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from enum import Enum
from openai import OpenAI

app = FastAPI()

client = OpenAI()


class Severity(str, Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    CRITICAL = "CRITICAL"

class Category(str, Enum):
    DATABASE = "DATABASE"
    NETWORK = "NETWORK"
    APPLICATION = "APPLICATION"
    INFRASTRUCTURE = "INFRASTRUCTURE"
    SECURITY = "SECURITY"

class IncidentAnalysis(BaseModel):
    severity: Severity
    category: Category
    summary: str
    suggested_actions: list[str]
    affected_services: list[str]
    requires_immediate_action: bool
    confidence: float = Field(ge=0, le=1)

@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "UP"}

class IncidentRequest(BaseModel):
    description: str = Field(min_length=10)

@app.post("/incidents/analyze", response_model=IncidentAnalysis)
def analyze_incidents(request: IncidentRequest) -> IncidentAnalysis:

    response = client.responses.parse(
        model="gpt-4o-mini",
        instructions=(
            "Analyze only facts explicitly stated in the incident description. "
            "Do not invent service names, incident impact, or root causes. "
            "If no service is named, return an empty affected_services list. "
            "Set requires_immediate_action to true only when the description "
            "explicitly reports a widespread outage, actual data loss, or an "
            "ongoing credential or secret leak; otherwise set it to false. "
            "Suggest checks rather than presenting unverified causes as facts."
        ),
        input=request.description,
        text_format=IncidentAnalysis,
    )
    analysis = response.output_parsed

    if analysis is None:
        raise HTTPException(status_code=502, detail="Incident analysis failed")
    return analysis
