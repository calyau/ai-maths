---
concept: Group Extension
slug: group-extension
category: homological-algebra
subcategory: group-theory
tier: advanced
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Introduction to Homological Algebra and Group Cohomology"
chapter_number: 17
pdf_page: 822
section: "17.4 Group Extensions, Factor Sets and H^2(G,A)"
extraction_confidence: high
aliases:
  - "extension of A by G"
prerequisites:
  - group-cohomology
extends: []
related:
  - factor-set
  - crossed-homomorphism
contrasts_with: []
answers_questions:
  - "What is a group extension?"
  - "What does H^2(G,A) classify?"
---

# Quick Definition
A group extension of A by G is a short exact sequence 1 → A → E → G → 1. The set of equivalence classes of extensions is in bijection with H^2(G,A).

# Core Definition
A **group extension** of the abelian group A by the group G is a short exact sequence 1 → A →^ι E →^π G → 1 where E is a group, ι is injective, π is surjective, and ι(A) = ker π (p. 822). Two extensions are **equivalent** if there is a group isomorphism between the middle terms compatible with A and G. The equivalence classes of extensions correspond bijectively with elements of H^2(G,A), with the split extension corresponding to 0.

# Prerequisites
- **group-cohomology** — H^2 classifies extensions

# Key Properties
1. H^2(G,A) = 0 implies every extension splits
2. The trivial element of H^2 corresponds to the semidirect product
3. Factor sets (2-cocycles) encode the multiplication in E

# Relationships
## Builds Upon
- **group-cohomology** — H^2(G,A) classifies extensions

## Related
- **factor-set** — Factor sets are the 2-cocycles representing extensions

# Source Reference
Chapter 17, Section 17.4, pages 822-840.

# Verification Notes
- Confidence: HIGH — major classification theorem
