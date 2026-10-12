Proposal Generator lets a freelancer or small agency turn a messy client brief into a client-ready proposal using a four-agent PydanticAI pipeline on Gemini.
MVP and success criteria:
Typed schemas: all four models import and validate.
Intake agent: returns a valid IntakeResult on 4 messy briefs and flags missing info instead of inventing it at least once.
Research and Draft agents: the proposal uses the real scope, budget and timeline from intake.
Reviewer with one retry: at least one brief triggers a revision, and the second draft addresses the feedback.
Orchestrator: python main.py runs the whole pipeline with step logging and no manual input.
Out of scope: web UI, pricing-lookup tool calls, memory across clients, per-agent model swapping, PDF/Word export, more than one retry.
Portfolio angle: shows  understanding of multi-agent design, meaning typed handoffs, separation of concerns, and failure handling like bounded retries and missing-info flags.