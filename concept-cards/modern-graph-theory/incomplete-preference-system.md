---
concept: Incomplete Preference System
slug: incomplete-preference-system
category: matchings
subcategory: stable-matchings
tier: advanced
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Flows, Connectivity and Matching"
chapter_number: 3
pdf_page: 74
section: "III.5 Stable Matchings"
extraction_confidence: high
aliases:
  - "incomplete system of preferences"
  - "Theorem 21"
prerequisites:
  - stable-matching
  - optimal-stable-matching
extends:
  - stable-matching
related:
  - college-admissions-problem
contrasts_with: []
answers_questions:
  - "How do stable matchings work with incomplete preferences?"
---

# Quick Definition
An incomplete preference system allows each person to have a partial preference list — they may be unwilling to marry some acquaintances. Stable complete matchings can be characterized via an associated complete system with a widower/widow trick.

# Core Definition
An incomplete system of preferences $(V_1, V_2, L)$ gives each person a possibly incomplete list of acceptable partners. A stable complete matching requires every matched pair to appear on each other's lists. **Theorem 21**: $(V_1, V_2, L)$ has a stable complete matching iff the associated complete system $(V_1', V_2', L')$ (with added widower and widow) has a stable matching in which widow marries widower (Bollobás, pp. 99-100).

# Prerequisites
- **Stable matching** — The generalized setting
- **Optimal stable matching** — Used in the associated system

# Key Properties
1. Add fictitious widower $w$ and widow $W$
2. Each person slots widow/widower after genuine preferences
3. A stable complete matching in the incomplete system corresponds to a stable matching in the complete system where $w$ marries $W$
4. If any stable matching in the complete system contains $wW$, all do (Theorem 21')

# Context & Application
Models real-world matching where participants have limited acceptability lists.

# Examples
**Example** (p. 100): The $V_1$-optimal stable matching in the associated system is the $V_2$-pessimal one. If it contains $wW$, then every stable matching does, so the incomplete system has a stable complete matching.

# Relationships
## Builds Upon
- **stable-matching** — Generalized to incomplete preferences

## Related
- **college-admissions-problem** — Another generalization

# Source Reference
Chapter III, Section III.5, pages 99-100. Theorems 21, 21'.

# Verification Notes
- Definition source: Direct from pp. 99-100
- Confidence rationale: Explicitly stated with proof
- Uncertainties: None
- Cross-reference status: Verified
