---
concept: Kernel
slug: kernel
category: group-theory
subcategory: morphisms
tier: intermediate
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Quotient Groups and Homomorphisms"
chapter_number: 3
pdf_page: 73
section: "3.1 Definitions and Examples"
extraction_confidence: high
aliases:
  - "$\\ker \\varphi$"
prerequisites:
  - homomorphism
extends: []
related:
  - normal-subgroup
  - quotient-group
  - first-isomorphism-theorem
contrasts_with: []
answers_questions:
  - "What is the kernel of a homomorphism?"
  - "How does the kernel relate to injectivity?"
---

# Quick Definition
The kernel of a homomorphism $\varphi: G \to H$ is $\ker\varphi = \{g \in G \mid \varphi(g) = 1_H\}$. It is always a normal subgroup of G, and $\varphi$ is injective iff $\ker\varphi = \{1\}$.

# Core Definition
If $\varphi: G \to H$ is a homomorphism, the *kernel* of $\varphi$ is $\ker\varphi = \{g \in G \mid \varphi(g) = 1_H\}$, the fiber over the identity of H. The kernel is a subgroup of G (Proposition 1) and is always a normal subgroup. Conversely, every normal subgroup is the kernel of some homomorphism (namely, the natural projection) (Dummit & Foote, pp. 74-85).

# Prerequisites
- **Homomorphism** — kernel is defined for homomorphisms

# Key Properties
1. $\ker\varphi \leq G$ (always a subgroup)
2. $\ker\varphi \trianglelefteq G$ (always normal)
3. $\varphi$ is injective iff $\ker\varphi = \{1\}$
4. The fibers of $\varphi$ are the cosets of $\ker\varphi$
5. $G/\ker\varphi \cong \varphi(G)$ (First Isomorphism Theorem)
6. Every normal subgroup is the kernel of the natural projection

# Context & Application
The kernel is the bridge between homomorphisms and normal subgroups. Computing kernels identifies normal subgroups; conversely, knowing a normal subgroup gives a quotient group.

# Examples
**Example 1** (p. 74): For $\varphi: \mathbb{Z} \to Z_n$ by $a \mapsto x^a$, $\ker\varphi = n\mathbb{Z}$.
**Example 2** (p. 83): For the "absolute value" map $Q_8 \to V_4$, $\ker\varphi = \{\pm 1\}$.

# Relationships
## Builds Upon
- **homomorphism**

## Enables
- **normal-subgroup** — kernels are normal
- **quotient-group** — $G/\ker\varphi$ is the quotient
- **first-isomorphism-theorem** — $G/\ker\varphi \cong \text{im}(\varphi)$

# Common Confusions
- **Confusion**: Thinking the kernel can be any subgroup. **Clarification**: The kernel of a homomorphism is always NORMAL. A non-normal subgroup cannot be a kernel.

# Source Reference
Chapter 3: Quotient Groups and Homomorphisms, Section 3.1, pages 74-76, Proposition 1.

# Verification Notes
- Definition source: direct from source p. 74
- Confidence rationale: explicitly defined
- Uncertainties: none
- Cross-reference status: verified
