---
concept: Gale-Shapley Algorithm
slug: gale-shapley-algorithm
category: matchings
subcategory: stable-matchings
tier: intermediate
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Flows, Connectivity and Matching"
chapter_number: 3
pdf_page: 74
section: "III.5 Stable Matchings"
extraction_confidence: high
aliases:
  - "fundamental algorithm"
  - "deferred acceptance algorithm"
  - "proposal algorithm"
prerequisites:
  - stable-matching
extends: []
related:
  - optimal-stable-matching
contrasts_with: []
answers_questions:
  - "How do I find a stable matching?"
---

# Quick Definition
The Gale-Shapley algorithm finds a stable matching by having boys propose to their highest-ranked remaining girls in rounds, while girls reject all but their best current suitor.

# Core Definition
The algorithm operates in rounds: in odd rounds, each boy proposes to his highest-preference girl who has not yet refused him; in even rounds, each girl refuses all but her highest suitor. The process ends when no girl refuses a suitor, and each girl marries her sole remaining suitor. The algorithm terminates after at most $2nm$ rounds (Bollobás, pp. 95-96).

# Prerequisites
- **Stable matching** — The algorithm produces a stable matching

# Key Properties
1. Always terminates (at most $m(n-1)$ refusals possible)
2. Produces a stable matching (Theorem 16)
3. The resulting matching is $V_1$-optimal (Theorem 20)
4. Simultaneously $V_2$-pessimal
5. Once a girl gets a proposal, she ends up married
6. As the algorithm progresses, girls get better suitors and boys get worse

# Construction / Recognition
1. Each boy proposes to his top-ranked girl who hasn't refused him
2. Each girl keeps her best suitor and refuses all others
3. Repeat until no refusals occur
4. Final proposals become the stable matching

# Context & Application
"It is rather quaint that this fundamental algorithm is simply the codification of the rules of old-fashioned etiquette" (p. 95). It solves the stable marriage problem and extends to college admissions.

# Examples
**Example** (p. 95): The algorithm can be run "at various speeds" — boys and girls may act individually rather than in synchronized rounds, and the result is independent of the speed.

# Relationships
## Builds Upon
- **stable-matching** — The algorithm produces one

## Enables
- **optimal-stable-matching** — The algorithm produces the $V_1$-optimal matching

# Common Errors
- **Error**: Running the algorithm with girls proposing instead of boys
  **Correction**: Swapping proposer/receiver roles produces the $V_2$-optimal (not $V_1$-optimal) matching

# Common Confusions
- **Confusion**: Thinking the speed of running matters
  **Clarification**: The algorithm produces the same result regardless of whether actions are synchronized or individual

# Source Reference
Chapter III, Section III.5, pages 95-96. Theorem 16.

# Verification Notes
- Definition source: Direct from pp. 95-96
- Confidence rationale: Explicitly described with proof of correctness
- Uncertainties: None
- Cross-reference status: Verified
