---
concept: Subgroup Criterion
slug: subgroup-criterion
category: group-theory
subcategory: subgroups
tier: intermediate
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Subgroups"
chapter_number: 2
pdf_page: 46
section: "2.1 Definition and Examples"
extraction_confidence: high
aliases:
  - "one-step subgroup test"
  - "two-step subgroup test"
prerequisites:
  - subgroup
extends: []
related:
  - subgroup
contrasts_with: []
answers_questions:
  - "How do I efficiently test whether a subset is a subgroup?"
---

# Quick Definition
A subset H of G is a subgroup iff (1) $H \neq \emptyset$ and (2) $xy^{-1} \in H$ for all $x, y \in H$. For finite H, it suffices to check nonemptiness and closure under multiplication.

# Core Definition
**Proposition 1 (Subgroup Criterion):** A subset H of a group G is a subgroup iff (1) $H \neq \emptyset$, and (2) for all $x, y \in H$, $xy^{-1} \in H$. Furthermore, if H is finite, then it suffices to check that H is nonempty and closed under multiplication (Dummit & Foote, pp. 47-48).

# Prerequisites
- **Subgroup** — this is the criterion for testing subgroup status

# Key Properties
1. One-step test: $H \neq \emptyset$ and $xy^{-1} \in H$ for all $x, y \in H$
2. For finite H: $H \neq \emptyset$ and $xy \in H$ suffices (inverses come for free)
3. The finite case works because $x, x^2, \ldots$ must eventually repeat, giving $x^n = 1$

# Construction / Recognition
## To Apply:
1. Show H is nonempty (usually: show $1 \in H$)
2. Take arbitrary $x, y \in H$ and show $xy^{-1} \in H$

# Context & Application
This is the standard tool for verifying subgroups and is used throughout the text whenever a new subgroup is introduced.

# Examples
**Example 1** (p. 48): Proving centralizers are subgroups uses the criterion.

# Relationships
## Builds Upon
- **subgroup**

# Source Reference
Chapter 2, Section 2.1, pages 47-48, Proposition 1.

# Verification Notes
- Definition source: direct from source pp. 47-48
- Confidence rationale: explicitly stated as a proposition
- Uncertainties: none
- Cross-reference status: verified
