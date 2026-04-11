---
concept: Module Isomorphism
slug: module-isomorphism
category: module-theory
subcategory: basic-definitions
tier: intermediate
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Introduction to Module Theory"
chapter_number: 10
pdf_page: 348
section: "10.2 Quotient Modules and Module Homomorphisms"
extraction_confidence: high
aliases:
  - "R-module isomorphism"
prerequisites:
  - module-homomorphism
extends:
  - group-isomorphism
related:
  - first-isomorphism-theorem
contrasts_with: []
answers_questions:
  - "When are two modules isomorphic?"
---

# Quick Definition
A module isomorphism is a bijective module homomorphism. Two modules are isomorphic if there exists an isomorphism between them.

# Core Definition
An R-module isomorphism is an R-module homomorphism $\varphi: M \to N$ that is bijective (both injective and surjective). Equivalently, it is a module homomorphism with an inverse that is also a module homomorphism. The First Isomorphism Theorem states that if $\varphi: M \to N$ is a module homomorphism, then $M/\ker\varphi \cong \varphi(M)$ (Dummit & Foote, p. 349).

# Prerequisites
- **module-homomorphism** — An isomorphism is a bijective homomorphism

# Key Properties
1. $M/\ker\varphi \cong \text{image}(\varphi)$ for any module homomorphism $\varphi$
2. The Second Isomorphism Theorem: $(A + B)/B \cong A/(A \cap B)$ for submodules A, B
3. The Third Isomorphism Theorem: $(M/A)/(B/A) \cong M/B$ for submodules $A \subseteq B$
4. The Lattice Isomorphism Theorem holds for modules

# Context & Application
The isomorphism theorems provide the fundamental tools for analyzing module structure, just as they do for groups and rings.

# Relationships
## Builds Upon
- **module-homomorphism**

## Related
- **first-isomorphism-theorem** — The key structural result

# Source Reference
Chapter 10, Section 10.2, pp. 349-350.

# Verification Notes
- Confidence: HIGH — standard definitions carrying over from group theory
