# Enterprise AI Incident Investigator

## Project purpose

**Enterprise AI Incident Investigator** is the capstone project for the AI Engineering — 90 Days course.

It simulates an enterprise production-support system that helps engineers investigate incidents by combining:

- incident metadata
- logs
- internal documentation
- runbooks
- deployment history
- service information
- LLM reasoning
- retrieval
- tool calling

The project is intentionally close to a real backend / microservices environment rather than a generic chatbot.

---

# Problem

Production incidents often require an engineer to manually collect information from multiple systems:

- incident management
- logs
- service documentation
- deployment history
- runbooks
- previous troubleshooting knowledge

The investigator must then correlate that information and form a root-cause hypothesis.

The goal of this project is to automate the **information gathering and evidence correlation** while keeping the result inspectable and grounded in sources.

---

# Core use case

Input:

> “Investigate incident INC-1024. Checkout API started returning HTTP 500 after the latest deployment.”

The system should:

1. Load the incident.
2. Identify affected services.
3. Retrieve relevant documentation and runbooks.
4. Search logs.
5. Check recent deployments.
6. Correlate the evidence.
7. Form one or more root-cause hypotheses.
8. Produce recommended next actions.
9. Return a structured report with evidence.

---

# High-level architecture

```text
                        ┌─────────────────────┐
                        │      Client/UI      │
                        └──────────┬──────────┘
                                   │
                                   ▼
                        ┌─────────────────────┐
                        │       FastAPI       │
                        │  Investigator API   │
                        └──────────┬──────────┘
                                   │
                                   ▼
                        ┌─────────────────────┐
                        │      LangGraph      │
                        │ Investigation Flow  │
                        └───────┬─────┬───────┘
                                │     │
                     ┌──────────┘     └──────────┐
                     ▼                           ▼
          ┌────────────────────┐      ┌────────────────────┐
          │        RAG         │      │       Tools        │
          │ PostgreSQL/pgvector│      │ incidents / logs   │
          └─────────┬──────────┘      │ deployments / etc. │
                    │                 └──────────┬─────────┘
                    │                            │
                    └──────────────┬─────────────┘
                                   ▼
                        ┌─────────────────────┐
                        │       LLM API       │
                        └──────────┬──────────┘
                                   │
                                   ▼
                        ┌─────────────────────┐
                        │ Structured Report   │
                        │ + Evidence/Citations│
                        └─────────────────────┘

Supporting components:

- MCP Server
- Langfuse observability
- pytest
- DeepEval
```

---

# Main technologies

## Backend

- Python
- FastAPI
- Pydantic
- Uvicorn

## AI

- LLM API
- Structured Outputs
- Embeddings
- RAG
- Tool Calling
- LangGraph

## Data

- PostgreSQL
- pgvector

## Integration

- MCP

## Quality

- pytest
- DeepEval

## Observability

- Langfuse
- structured application logs

## Deployment

- Docker
- Docker Compose

---

# Planned services / modules

```text
app/
├── api/
│   ├── health.py
│   └── incidents.py
├── models/
│   ├── incident.py
│   └── investigation.py
├── services/
│   ├── llm.py
│   ├── retrieval.py
│   └── investigation.py
├── tools/
│   ├── incidents.py
│   ├── logs.py
│   ├── deployments.py
│   └── runbooks.py
├── graph/
│   ├── state.py
│   └── investigator.py
├── mcp/
│   └── server.py
├── evals/
├── tests/
└── main.py
```

The structure can evolve as implementation progresses.

---

# Domain model

## Incident

Example fields:

```json
{
  "id": "INC-1024",
  "title": "Checkout API returns HTTP 500",
  "severity": "SEV2",
  "service": "checkout-api",
  "started_at": "2026-11-17T14:32:00Z",
  "description": "Error rate increased after deployment."
}
```

## Investigation result

Example structure:

```json
{
  "incident_id": "INC-1024",
  "summary": "Checkout failures started immediately after deployment v2.18.0.",
  "suspected_root_cause": "Database connection configuration regression.",
  "confidence": 0.88,
  "affected_services": [
    "checkout-api"
  ],
  "evidence": [
    {
      "source": "logs",
      "detail": "Connection pool initialization failures started at 14:31."
    },
    {
      "source": "deployment",
      "detail": "Version v2.18.0 was deployed at 14:29."
    }
  ],
  "recommended_actions": [
    "Rollback checkout-api to v2.17.4",
    "Compare database configuration between releases"
  ]
}
```

---

# Synthetic enterprise data

The project will not depend on confidential company systems.

We will create synthetic data representing:

- incidents
- application logs
- deployment events
- service catalog information
- runbooks
- architecture documentation
- troubleshooting documentation

This makes the repository safe to publish as a portfolio project.

---

# Planned tools

The AI workflow should eventually be able to call:

## `get_incident`

Returns structured incident metadata.

## `search_logs`

Searches synthetic application logs.

## `get_recent_deployments`

Returns deployment history for a service.

## `get_service_info`

Returns service ownership and dependency information.

## `search_runbooks`

Retrieves relevant operational documentation.

---

# Investigation workflow

Target LangGraph flow:

```text
START
  │
  ▼
Load Incident
  │
  ▼
Classify Incident
  │
  ▼
Build Initial Context
  │
  ├────► Search Documentation
  │
  ├────► Search Logs
  │
  └────► Check Deployments
  │
  ▼
Correlate Evidence
  │
  ▼
Generate Hypothesis
  │
  ▼
Validate Evidence
  │
  ▼
Generate Final Report
  │
  ▼
END
```

---

# RAG knowledge base

The knowledge base will contain synthetic documents such as:

```text
docs/
├── services/
│   ├── checkout-api.md
│   └── payment-api.md
├── runbooks/
│   ├── database-connections.md
│   └── kafka-consumer-lag.md
└── architecture/
    └── checkout-flow.md
```

Documents will be:

1. loaded
2. chunked
3. embedded
4. stored in PostgreSQL/pgvector
5. retrieved during investigations

---

# MCP

The project will expose selected capabilities through an MCP server.

Possible MCP tools:

- `get_incident`
- `search_logs`
- `get_recent_deployments`
- `search_runbooks`

The MCP layer should expose safe, typed, preferably read-only enterprise tools.

---

# Observability

Each investigation should eventually capture:

- request ID
- graph execution
- LLM calls
- prompts
- responses
- tool calls
- retrieval results
- latency
- token usage
- failures

Langfuse will be used for AI-specific tracing.

---

# Evaluation strategy

The repository will contain synthetic test cases.

Example:

```text
Incident:
Checkout API failures after deployment.

Expected evidence:
- deployment occurred immediately before errors
- logs contain DB connection failures

Expected root cause:
database configuration regression
```

Tests should evaluate:

- correct structured output
- correct tool selection
- retrieval relevance
- evidence grounding
- final-answer quality
- regression between prompt/model changes

---

# Security principles

The system should demonstrate:

- validated inputs
- validated LLM outputs
- read-only tools where possible
- authorization boundaries
- protection against prompt injection
- protection against indirect prompt injection
- tool allowlists
- timeouts
- retry limits
- maximum graph iterations
- no secrets in prompts/logs/repository

---

# Portfolio goal

The final repository should demonstrate that the author can combine traditional backend engineering with modern AI application engineering.

A reviewer should be able to see practical knowledge of:

- backend API design
- typed contracts
- LLM integration
- RAG
- vector databases
- agent/tool patterns
- LangGraph
- MCP
- evaluation
- observability
- security
- deployment

---

# Current status

**Week 1 — project initialization**

Not yet implemented:

- [ ] FastAPI application
- [ ] Incident models
- [ ] Investigation models
- [ ] LLM integration
- [ ] PostgreSQL
- [ ] pgvector
- [ ] RAG
- [ ] tools
- [ ] LangGraph
- [ ] MCP
- [ ] Langfuse
- [ ] evaluations
- [ ] Docker deployment
