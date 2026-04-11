---
concept: First Isomorphism Theorem
slug: first-isomorphism-theorem
category: group-theory
subcategory: isomorphism-theorems
tier: intermediate
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Quotient Groups and Homomorphisms"
chapter_number: 3
pdf_page: 73
section: "3.3 The Isomorphism Theorems"
extraction_confidence: high
aliases:
  - "Fundamental Theorem of Homomorphisms"
prerequisites:
  - homomorphism
  - kernel
  - quotient-group
  - normal-subgroup
extends: []
related:
  - second-isomorphism-theorem
  - third-isomorphism-theorem
  - fourth-isomorphism-theorem
contrasts_with: []
answers_questions:
  - "How does the kernel of a homomorphism relate to quotient groups?"
  - "What is the First Isomorphism Theorem?"
---

# Quick Definition
If $\varphi: G \to H$ is a homomorphism, then $\ker\varphi \trianglelefteq G$ and $G/\ker\varphi \cong \varphi(G)$. Every quotient group is isomorphic to the image of some homomorphism, and vice versa.

# Core Definition
**Theorem 16 (First Isomorphism Theorem):** If $\varphi: G \to H$ is a homomorphism of groups, then $\ker\varphi \trianglelefteq G$ and $G/\ker\varphi \cong \varphi(G)$. Corollary 17: (1) $\varphi$ is injective iff $\ker\varphi = 1$; (2) $|G : \ker\varphi| = |\varphi(G)|$ (Dummit & Foote, p. 97).

# Prerequisites
- **Homomorphism** — the theorem applies to homomorphisms
- **Kernel** — the kernel is a normal subgroup
- **Quotient group** — the quotient by the kernel
- **Normal subgroup** — the kernel is always normal

# Key Properties
1. $\ker\varphi$ is always a normal subgroup of the domain
2. The quotient $G/\ker\varphi$ is naturally isomorphic to the image $\varphi(G)$
3. $\varphi$ is injective iff $\ker\varphi = \{1\}$
4. $|G:\ker\varphi| = |\varphi(G)|$ (index = image size)
5. This generalizes the dimension formula: $\dim V = \text{rank } \varphi + \text{nullity } \varphi$

# Construction / Recognition
## To Apply:
1. Identify a homomorphism $\varphi: G \to H$
2. Compute $\ker\varphi$
3. Conclude $G/\ker\varphi \cong \varphi(G)$

# Context & Application
The First Isomorphism Theorem is the fundamental bridge between homomorphisms and quotient groups. It shows that every homomorphic image of G is a quotient of G, and vice versa. This is used constantly in group theory.

# Examples
**Example 1** (p. 97): The sign map $\epsilon: S_n \to \{\pm 1\}$ has kernel $A_n$, so $S_n/A_n \cong \mathbb{Z}_2$.
**Example 2** (p. 97): The determinant map $\det: GL_n(F) \to F^\times$ has kernel $SL_n(F)$, so $GL_n(F)/SL_n(F) \cong F^\times$.

# Relationships
## Builds Upon
- **homomorphism**, **kernel**, **quotient-group**, **normal-subgroup**

## Enables
- **second-isomorphism-theorem** — the Diamond Isomorphism Theorem
- **third-isomorphism-theorem** — quotients of quotients

## Related
- **fourth-isomorphism-theorem** — lattice correspondence

# Common Errors
- **Error**: Applying the theorem without verifying $\varphi$ is a homomorphism. **Correction**: Always check the homomorphism property first.

# Common Confusions
- **Confusion**: Thinking the isomorphism $G/\ker\varphi \cong \varphi(G)$ means $G/\ker\varphi \cong H$. **Clarification**: The isomorphism is with the IMAGE $\varphi(G)$, which may be a proper subgroup of H.

# Source Reference
Chapter 3: Quotient Groups and Homomorphisms, Section 3.3, page 97, Theorem 16, Corollary 17.

# Verification Notes
- Definition source: direct from source p. 97
- Confidence rationale: major theorem, explicitly stated
- Uncertainties: none
- Cross-reference status: verified
