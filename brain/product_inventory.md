# NeetiQ Product Inventory (Source of Truth)
> This file tells Direction Bots what's ACTUALLY built vs planned.
> Updated: 2026-04-05 by Admin Agent (DPDP Compliance Command Center added per Avi)
> ALL direction bots MUST read this before making product recommendations.

---

## ContraRed (Contract Intelligence Module)

### BUILT AND WORKING
- **Word Add-in**: Full Microsoft Word native integration. Intelligence arrives where work happens.
- **Contract review engine**: Clause-by-clause scanning, risk detection, summary generation.
- **Clause detection**: Identifies and classifies clauses across contract types.
- **Fix generation**: AI-generated revision suggestions for flagged clauses, grounded in legal principles.
- **OOXML Track Changes**: Generates real Word track changes, not a separate report.
- **Playbook engine**: 106 rules across 10 Indian contract types (NDA, MSA, SaaS, Employment, + 6 more). Encodes review standards and applies consistently.
- **Risk card generation**: Visual risk flagging with statutory references.
- **Dashboard (web URL)**: Batch upload, multi-contract analysis, contract comparison.
- **Agentic Draft Agent**: Can draft contracts from scratch based on active inputs (party details, terms, type). Fully functional.
- **DPDP Compliance Command Center** (NEW, built Apr 2026): Full end-to-end DPDP compliance automation. 5 AI agents:
  - Scanner Agent: Scans contracts against 18 DPDP rules (hybrid: deterministic keyword/regex + Vertex AI semantic). Single + bulk (up to 100 contracts).
  - Gap Assessor Agent: 30-question assessment across 10 DPDP categories (Sections 4-17). Auto-answers consent questions from real consent data.
  - Remediation Agent: Generates 7 DPDP-compliant document types (DPA, privacy notice, consent form, breach notifications, contract clauses, policy updates, process recommendations). English + Hindi.
  - Monitor Agent: Real-time compliance dashboard, 6 DPDP deadline alerts, compliance drift detection, SLA tracking.
  - Rights Agent: Data Principal rights lifecycle (90-day SLA), grievances (30-day SLA), nominations (Section 14), auto-escalation.
  - Supporting: Consent Compliance Bridge, in-memory DPDP Knowledge Base (Act + Rules 2025), audit-ready report generation (10-section output).
  - 22 API endpoints. 8 penalty categories tracked. Zero data retention mode. ISO 27560 consent receipts with HMAC-SHA256.
  - Dashboard UI: 5 tabs (Overview, Scan, Assess, Remediate, Report).
- **Section 27 (restraint of trade) enforceability checks**
- **Indian Contract Act clause scanning**
- **Template library**: 10+ Indian contract templates

### IN DEVELOPMENT
- Custom playbook creation (let firms define their own rules)
- Document version control and comparison

### PLANNED / NOT BUILT YET
- Real-time regulatory tracking (auto-update when statutes change)
- Multi-jurisdiction support beyond India
- Enterprise SSO and advanced org management
- MCP integration with Smriti (cross-product queries)

---

## Smriti (Litigation Intelligence Module)

### BUILT AND WORKING
- **Multi-step agentic research pipeline** (LangGraph architecture):
  - User inputs query
  - Query expanded using bare acts and statutes
  - Multiple agents run in parallel across PostgreSQL and vector database (Pinecone)
  - Indian Kanoon API bot fills gaps for HC/tribunal cases
  - Web search bot fills additional gaps
  - All research compiled
  - Cohere reranking gives top results
  - Gap analysis model checks for missing coverage, can re-run agents with specific queries
- **Case database**: ~3,000 SC cases ingested (2023-2026 era). Planning to ingest ALL Supreme Court cases soon, then top 5 High Courts (Delhi, Bombay, Madras, Calcutta, Karnataka).
- **Vector database** (Pinecone): Semantic search across case corpus.
- **PostgreSQL**: Case metadata, full-text storage.
- **Neo4j citation graph**: Maps which cases cite which. Used for precedent chains and connected case discovery.
- **Judge probabilistic system**: Analyzes judge tendencies and case outcome patterns.
- **Indian Kanoon API integration**: Supplementary case law source.
- **Web search bot**: Finds HC and tribunal cases beyond indexed corpus.
- **Cohere reranking**: Improves search relevance.
- **Gap analysis with agent re-run**: If research has gaps, automatically re-queries with targeted queries.
- **Gemini API**: Embeddings and LLM processing.
- **Zero hallucinated citations**: Architectural, every citation traces to specific judgment paragraph.
- **Case viewer with citation graph visualization**
- **Freemium model**: Free tier (5 queries/day) + Paid tier (₹999/month)

### IN DEVELOPMENT
- **Argument generation agent**: Multi-agentic approach similar to research pipeline. Will auto-generate legal arguments grounded in researched case law. In progress.
- **Expanding case database**: From 3K to 50K+ SC cases, then HCs.

### PLANNED / NOT BUILT YET
- **Drafting agent**: Litigation-focused document drafting (unlike ContraRed's contract drafting). Will generate petitions, replies, applications grounded in cited authority.
- **MCP integration with ContraRed**: Connect both products. Example: ContraRed finds a risky clause, queries Smriti's database to check actual judicial interpretation and enforceability.
- **Hindi language support**
- **Manupatra / SCC integration** (beyond Indian Kanoon)
- **Advanced citation network visualization**
- **Legal research collaboration features** (multi-user workspaces)
- **Mobile app** (deferred)

---

## Cross-Platform (NeetiQ OS level)

### PLANNED
- Unified authentication (single login for ContraRed + Smriti)
- Unified dashboard combining research + contracts + drafting + analytics
- MCP bridge between ContraRed and Smriti
- Custom Intelligence modules (enterprise bespoke)
- Regulatory tracking module (standalone)

---

## Tech Stack
- **Backend**: Python, LangGraph (agent orchestration), Gemini API
- **Databases**: PostgreSQL, Pinecone (vector), Neo4j (graph)
- **AI/ML**: Gemini (embeddings + LLM), Cohere (reranking)
- **Frontend**: Web dashboard, Microsoft Word Add-in (OOXML)
- **APIs**: Indian Kanoon, web scraping for HC/tribunals
- **Infrastructure**: GCP (credits), Render (backend), Netlify/Vercel (frontend)

---

## Key Numbers
- ContraRed: 106 playbook rules, 10 contract types, 10x faster review
- Smriti: 3K cases indexed (target 50K+), 8-12 hours saved per research cycle
- Burn rate: ~₹25K/month
- Current users: ~30-40 freemium signups (Nov-Dec period)
- Paying customers: Zero (pilot stage)
- Pricing target: ₹5K-8K/user/month enterprise
