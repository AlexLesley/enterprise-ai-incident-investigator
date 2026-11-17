# AI Engineering — 90 Days Roadmap

## Goal

Transition from **Senior Java Backend Engineer** to **Backend / AI Application Engineer** in 12 weeks.

The focus is not on ML research or model training. The goal is to learn how to build, test, secure, observe and deploy production AI applications using the backend engineering skills already in place: APIs, microservices, Kafka, databases, containers, OpenShift and distributed systems.

Time commitment: **1–2 hours per day**.

Main capstone: **Enterprise AI Incident Investigator**.

---

## Learning principles

- Build something every week.
- Prefer production-oriented patterns over toy notebooks.
- Use Python as an application language, not as an academic subject.
- Keep the architecture close to real enterprise backend systems.
- Reuse the same capstone throughout the course.
- Every week should leave a demonstrable artifact in Git.

---

# Week 1 — Python for Backend Engineers + FastAPI

## Goal

Become productive enough in Python to build typed backend APIs without spending weeks studying the entire language.

## Topics

- Python project structure
- Virtual environments
- `uv` / `pip`
- Type hints
- `dataclasses`
- Exceptions
- Async basics
- HTTP APIs
- FastAPI
- Pydantic
- Request/response validation
- Dependency injection basics
- Environment configuration
- pytest basics

## Technologies

- Python 3.12+
- FastAPI
- Pydantic
- Uvicorn
- pytest
- HTTPX

## Expected result

A working FastAPI service with typed request/response models, validation, configuration and tests.

## Capstone milestone

Create the initial **Incident Investigator API** with endpoints such as:

- `POST /incidents/analyze`
- `GET /incidents/{id}`
- `GET /health`

---

# Week 2 — LLM APIs + Structured Outputs

## Goal

Learn how backend applications communicate reliably with LLMs.

## Topics

- LLM API fundamentals
- Prompts vs messages
- System / user messages
- Tokens
- Temperature and deterministic behavior
- JSON outputs
- Structured Outputs
- Pydantic schemas for LLM responses
- Retries
- Timeouts
- Error handling
- Rate limits
- Cost awareness
- Prompt versioning

## Technologies

- OpenAI API or compatible enterprise LLM API
- Pydantic
- FastAPI
- HTTPX

## Expected result

The application can send incident information to an LLM and receive a validated structured response instead of free-form text.

## Capstone milestone

Return a typed incident analysis containing fields such as:

- summary
- suspected root cause
- affected services
- evidence
- confidence
- recommended next actions

---

# Week 3 — Embeddings + Vector Search

## Goal

Understand semantic search and build the retrieval layer used by modern AI applications.

## Topics

- Embeddings
- Cosine similarity
- Chunking
- Metadata
- Vector databases
- Semantic search
- Hybrid search concepts
- Retrieval quality
- Top-K
- Filtering
- Indexing pipelines

## Technologies

- PostgreSQL
- pgvector
- Embedding API
- SQLAlchemy or direct PostgreSQL client

## Expected result

Store internal documentation as embeddings and retrieve relevant chunks for a user query or incident.

## Capstone milestone

Add a searchable knowledge base containing synthetic:

- runbooks
- service documentation
- troubleshooting guides
- architecture notes

---

# Week 4 — Production RAG

## Goal

Turn vector search into a reliable Retrieval-Augmented Generation pipeline.

## Topics

- RAG architecture
- Query → retrieve → generate
- Context construction
- Citations
- Source attribution
- Chunking strategies
- Retrieval filters
- Reranking concepts
- Hallucination reduction
- Prompt injection through retrieved documents
- RAG failure modes

## Technologies

- FastAPI
- PostgreSQL + pgvector
- LLM API
- Embeddings

## Expected result

A complete RAG endpoint that produces answers grounded in internal documentation and includes supporting evidence.

## Capstone milestone

Incident Investigator can use internal runbooks and documentation while generating an incident diagnosis.

---

# Week 5 — Tool Calling + Agent Loops

## Goal

Move from “LLM answers questions” to “LLM can interact with systems”.

## Topics

- Function / tool calling
- Tool schemas
- Deterministic tools
- Agent loop
- Tool selection
- Tool result validation
- Retry strategies
- Maximum iteration limits
- Side-effect safety
- Read-only vs write tools

## Technologies

- LLM tool calling
- FastAPI
- Pydantic
- Python functions / service clients

## Expected result

An AI workflow that decides when it needs additional information and calls backend tools to obtain it.

## Capstone milestone

Create tools such as:

- `get_incident`
- `get_service_info`
- `search_logs`
- `search_runbooks`
- `get_recent_deployments`

---

# Week 6 — LangGraph + Stateful AI Workflows

## Goal

Build AI workflows as explicit, testable state machines instead of uncontrolled agent loops.

## Topics

- Graph-based AI workflows
- Nodes
- Edges
- State
- Conditional routing
- Checkpoints
- Retry paths
- Human-in-the-loop concepts
- Deterministic + LLM hybrid workflows

## Technologies

- LangGraph
- FastAPI
- Pydantic

## Expected result

A multi-step investigation workflow whose execution path is visible and testable.

## Capstone milestone

Create an investigation graph:

1. Load incident
2. Classify problem
3. Retrieve documentation
4. Query logs/tools
5. Correlate evidence
6. Produce root-cause hypothesis
7. Generate final incident report

---

# Week 7 — MCP

## Goal

Understand the Model Context Protocol and expose enterprise capabilities to AI clients in a standardized way.

## Topics

- MCP architecture
- MCP server
- Tools
- Resources
- Prompts
- Transport concepts
- Security boundaries
- Tool contracts
- Connecting external AI clients

## Technologies

- MCP SDK
- Python
- FastAPI or supporting service APIs

## Expected result

A working MCP server exposing safe enterprise-style tools.

## Capstone milestone

Create an **Incident MCP Server** exposing tools such as:

- incident lookup
- log search
- service metadata
- runbook search

---

# Week 8 — Evals + Testing AI Systems

## Goal

Learn how to test an AI application when outputs are probabilistic.

## Topics

- Unit tests vs AI evals
- Golden datasets
- Regression tests
- Retrieval evaluation
- Answer relevance
- Faithfulness / groundedness
- Tool-call correctness
- Structured-output validation
- LLM-as-judge concepts
- Offline evaluation

## Technologies

- pytest
- DeepEval or equivalent evaluation framework
- Pydantic

## Expected result

A repeatable evaluation suite that detects quality regressions.

## Capstone milestone

Create a synthetic evaluation dataset of incidents and expected investigation behavior.

---

# Week 9 — Context Engineering

## Goal

Learn how to control what information the model sees and how that affects quality, cost and reliability.

## Topics

- Context windows
- Context selection
- Prompt structure
- Dynamic context
- Conversation memory concepts
- Summarization
- Evidence prioritization
- Token budgets
- Context compression
- Long-context failure modes

## Technologies

- LLM API
- LangGraph
- RAG stack

## Expected result

A deliberate context-building layer instead of simply sending every available document to the model.

## Capstone milestone

Build an **Investigation Context Builder** that selects:

- incident data
- relevant logs
- relevant runbooks
- deployment information
- previous investigation evidence

---

# Week 10 — Observability

## Goal

Make AI workflows observable like production distributed systems.

## Topics

- Tracing
- Prompt traces
- Tool-call traces
- Latency
- Token usage
- Cost
- Errors
- Retrieval inspection
- Graph execution inspection
- Correlation IDs
- Debugging failed AI runs

## Technologies

- Langfuse
- Structured logging
- FastAPI
- LangGraph

## Expected result

Every investigation can be inspected from incoming request to final answer.

## Capstone milestone

Add observability for:

- LLM calls
- retrieval
- tools
- graph nodes
- latency
- token usage
- failures

---

# Week 11 — AI Security + Reliability

## Goal

Apply enterprise backend security thinking to AI applications.

## Topics

- Prompt injection
- Indirect prompt injection
- Tool abuse
- Data leakage
- Sensitive data
- Authorization
- Tool allowlists
- Read-only tools
- Output validation
- Rate limiting
- Timeouts
- Circuit breakers
- Fallback strategies
- Failure isolation

## Technologies

- FastAPI security patterns
- Pydantic validation
- Application-level authorization
- AI guardrails where appropriate

## Expected result

A documented threat model and hardened AI workflow.

## Capstone milestone

Protect Incident Investigator against malicious retrieved content and unsafe tool execution.

---

# Week 12 — Deployment + Portfolio

## Goal

Turn the capstone into a deployable portfolio project that demonstrates AI engineering skills to employers.

## Topics

- Docker
- Environment configuration
- Production API configuration
- PostgreSQL
- Deployment architecture
- Health checks
- CI concepts
- README
- Architecture diagrams
- Demo scenarios
- Interview explanation
- CV positioning

## Technologies

- Docker
- Docker Compose
- PostgreSQL + pgvector
- FastAPI
- LangGraph
- Langfuse
- pytest
- DeepEval
- GitHub

## Expected result

A runnable repository that can be cloned, started and demonstrated.

## Final capstone

**Enterprise AI Incident Investigator**

The system should:

- accept or load an incident
- retrieve relevant internal documentation
- query logs and enterprise-style tools
- correlate evidence
- generate a structured investigation
- cite supporting evidence
- expose tools through MCP
- execute the workflow through LangGraph
- record traces and metrics
- run automated AI evaluations
- include security controls
- run locally through Docker

---

# Definition of Done after 90 days

By the end of the course you should be able to explain and implement:

- FastAPI production APIs
- Pydantic typed contracts
- LLM API integration
- Structured Outputs
- Embeddings
- pgvector
- RAG
- Tool calling
- Agent loops
- LangGraph
- MCP
- AI evaluations
- Context engineering
- AI observability
- AI security
- Dockerized AI services

And, most importantly, you should have one substantial project that connects these concepts into a realistic backend system.
