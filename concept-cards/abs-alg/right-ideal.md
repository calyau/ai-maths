---
concept: Right Ideal
slug: right-ideal
category: ring-theory
subcategory: ideals
tier: intermediate
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Introduction to Rings"
chapter_number: 7
pdf_page: 243
section: "7.3 Ring Homomorphisms and Quotient Rings"
extraction_confidence: high
aliases: []
prerequisites:
  - ring
  - subring
extends:
  - subring
related:
  - ideal
  - left-ideal
contrasts_with:
  - left-ideal
answers_questions:
  - "What is a right ideal?"
---

# Quick Definition
A right ideal I of a ring R is a subring closed under right multiplication by all elements of R: $Ir \subseteq I$ for all $r \in R$.

# Core Definition
A subset I of R is a *right ideal* if (i) I is a subring of R, and (ii) $Ir \subseteq I$ for all $r \in R$ (Dummit & Foote, p. 244).

# Prerequisites
- **Ring** — Right ideals are subsets of rings
- **Subring** — Must be a subring

# Key Properties
1. For commutative rings, right = left = two-sided
2. In $M_n(R)$: row ideals are right ideals but not left ideals

# Relationships

## Related
- **ideal** — A two-sided ideal is both left and right
- **left-ideal** — Closed under left multiplication

# Source Reference
Chapter 7, Section 7.3, Definition (2)', page 244.

# Verification Notes
- Definition: Direct from p. 244
- Confidence: HIGH — explicit definition
