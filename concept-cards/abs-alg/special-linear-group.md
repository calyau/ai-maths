---
concept: Special Linear Group
slug: special-linear-group
category: group-theory
subcategory: important-groups
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
  - "$SL_n(F)$"
prerequisites:
  - general-linear-group
  - subgroup
extends:
  - general-linear-group
related:
  - normal-subgroup
  - simple-group
contrasts_with: []
answers_questions:
  - "What is the special linear group?"
---

# Quick Definition
$SL_n(F) = \{A \in GL_n(F) \mid \det(A) = 1\}$ is the subgroup of matrices with determinant 1. It is a normal subgroup of $GL_n(F)$ with $GL_n(F)/SL_n(F) \cong F^\times$.

# Core Definition
The *special linear group* is $SL_n(F) = \{A \in GL_n(F) \mid \det(A) = 1\}$. It is a subgroup of $GL_n(F)$ because $\det(AB) = \det(A)\det(B) = 1$ and $\det(A^{-1}) = 1/\det(A) = 1$. It is normal in $GL_n(F)$ since it is the kernel of the determinant homomorphism $\det: GL_n(F) \to F^\times$. By the First Isomorphism Theorem, $GL_n(F)/SL_n(F) \cong F^\times$ (Dummit & Foote, Exercises in Sections 2.1 and 3.3).

# Prerequisites
- **General linear group**, **Subgroup**

# Key Properties
1. $SL_n(F) \trianglelefteq GL_n(F)$
2. $GL_n(F)/SL_n(F) \cong F^\times$
3. $SL_n(F)/Z(SL_n(F))$ is simple for most n and F
4. If $|F| = q$, then $|GL_n(F) : SL_n(F)| = q - 1$

# Context & Application
$SL_n(F)/Z(SL_n(F))$ forms one of the 18 infinite families of finite simple groups.

# Relationships
## Builds Upon
- **general-linear-group**, **subgroup**

## Related
- **normal-subgroup** — $SL_n(F)$ is the kernel of det
- **simple-group** — quotient by center gives simple groups

# Source Reference
Chapter 2, Section 2.1, Exercise 9; Chapter 3, Section 3.3, Exercise 1.

# Verification Notes
- Definition source: from exercises in source
- Confidence rationale: defined in exercises, confirmed as kernel of det
- Uncertainties: none
- Cross-reference status: verified
