---
concept: Maximal Matching
slug: maximal-matching
category: matchings
subcategory: basic-definitions
tier: foundational
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Flows, Connectivity and Matching"
chapter_number: 3
pdf_page: 74
section: "III.5 Stable Matchings"
extraction_confidence: high
aliases:
  - "maximal matching"
prerequisites:
  - matching
extends:
  - matching
related:
  - maximum-matching
  - stable-matching
contrasts_with:
  - maximum-matching
answers_questions:
  - "What is the difference between maximal and maximum matching?"
---

# Quick Definition
A maximal matching is one that cannot be enlarged by adding another edge (no edge can be added while maintaining independence).

# Core Definition
A maximal matching in $G$ is a matching that cannot be enlarged to a strictly larger matching — no unmatched edge has both endpoints unmatched. Every stable matching is a maximal matching, but a maximal matching need not be maximum (largest cardinality) (Bollobás, p. 94).

# Prerequisites
- **Matching** — A maximal matching is a special matching

# Key Properties
1. Cannot add any edge without violating independence
2. Not necessarily of maximum cardinality
3. Every stable matching is maximal (p. 94)
4. A greedy approach always yields a maximal matching

# Context & Application
Maximal matchings arise naturally in greedy algorithms and stability conditions.

# Examples
**Example** (p. 94, Fig. III.8): $M = \{aB\}$ is a maximal matching (cannot be extended) but not a maximum matching.

# Relationships
## Builds Upon
- **matching** — A maximal matching is a matching

## Contrasts With
- **maximum-matching** — Maximum = largest cardinality; maximal = cannot be extended

## Related
- **stable-matching** — Every stable matching is maximal

# Common Confusions
- **Confusion**: Thinking "maximal" means "maximum"
  **Clarification**: Maximal = cannot be extended; maximum = largest possible size

# Source Reference
Chapter III, Section III.5, page 94.

# Verification Notes
- Definition source: Direct from p. 94
- Confidence rationale: Explicitly used
- Uncertainties: None
- Cross-reference status: Verified
