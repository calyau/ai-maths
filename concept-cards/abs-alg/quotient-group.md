---
concept: Quotient Group
slug: quotient-group
category: group-theory
subcategory: quotients
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
  - "factor group"
  - "$G/N$"
prerequisites:
  - normal-subgroup
  - coset
  - homomorphism
extends: []
related:
  - kernel
  - first-isomorphism-theorem
  - natural-projection
contrasts_with: []
answers_questions:
  - "What is a quotient group?"
  - "How do I construct a quotient group?"
  - "How do normal subgroups relate to quotient groups?"
  - "What must I know before understanding quotient groups?"
---

# Quick Definition
The quotient group G/N (G mod N) is the group whose elements are the cosets of a normal subgroup N, with multiplication $uN \cdot vN = (uv)N$. It "collapses" N to the identity.

# Core Definition
Let $\varphi: G \to H$ be a homomorphism with kernel K. The *quotient group* $G/K$ is the group whose elements are the fibers (= left cosets) of $\varphi$, with the operation: the product of the fiber over a and the fiber over b is the fiber over ab. Equivalently, if $N \trianglelefteq G$, then $G/N$ is the set of left cosets $\{gN \mid g \in G\}$ with operation $uN \cdot vN = (uv)N$. This is well defined iff $N \trianglelefteq G$ (Theorem 3, Proposition 5). The natural projection $\pi: G \to G/N$ by $g \mapsto gN$ is a surjective homomorphism with kernel N (Dummit & Foote, pp. 73-85).

# Prerequisites
- **Normal subgroup** — G/N requires $N \trianglelefteq G$
- **Coset** — elements of G/N are cosets
- **Homomorphism** — quotient groups arise from kernels of homomorphisms

# Key Properties
1. $|G/N| = |G:N| = |G|/|N|$ for finite G
2. The identity in G/N is the coset $1N = N$
3. $(gN)^{-1} = g^{-1}N$
4. $(gN)^\alpha = g^\alpha N$ for all $\alpha \in \mathbb{Z}$
5. The order of $gN$ in G/N is the smallest positive n with $g^n \in N$
6. Quotients of abelian groups are abelian; quotients of cyclic groups are cyclic
7. G/N is naturally isomorphic to $\text{im}(\varphi)$ where $\ker\varphi = N$

# Construction / Recognition
## To Construct/Create:
1. Verify $N \trianglelefteq G$
2. List the distinct cosets $gN$
3. Multiply cosets by multiplying representatives: $uN \cdot vN = (uv)N$

## To Identify/Recognize:
1. A group whose elements are cosets of a normal subgroup
2. The image of a surjective homomorphism from G

# Context & Application
Quotient groups are one of two fundamental tools (along with subgroups) for analyzing group structure. The study of quotient groups is equivalent to the study of homomorphic images. They enable inductive arguments on group order and are central to the Holder program for classifying finite groups.

# Examples
**Example 1** (p. 73): $\mathbb{Z}/n\mathbb{Z}$ is the quotient of $\mathbb{Z}$ by $n\mathbb{Z}$, with cosets $a + n\mathbb{Z}$.
**Example 2** (p. 84): $D_8/Z(D_8) \cong V_4$ since every nonidentity element of the quotient has order 2.
**Example 3** (p. 83): $Q_8/\langle -1 \rangle \cong V_4$.

# Relationships
## Builds Upon
- **normal-subgroup**, **coset**, **homomorphism**

## Enables
- **first-isomorphism-theorem** — $G/\ker\varphi \cong \text{im}(\varphi)$
- **composition-series** — successive quotients
- **simple-group** — groups with no nontrivial quotients

## Related
- **kernel** — the normal subgroup being collapsed
- **natural-projection** — the canonical map $G \to G/N$

# Common Errors
- **Error**: Trying to form G/N when N is not normal. **Correction**: The coset operation is well defined ONLY when $N \trianglelefteq G$.
- **Error**: Confusing elements of G/N with elements of G. **Correction**: Elements of G/N are COSETS (subsets of G), not individual elements of G.

# Common Confusions
- **Confusion**: Thinking G/N and N together determine G up to isomorphism. **Clarification**: Groups with isomorphic quotients and kernels may not be isomorphic (e.g., $D_8$ and $Q_8$ both have $V_4$ as quotient by center and $Z_2$ as center).

# Source Reference
Chapter 3: Quotient Groups and Homomorphisms, Section 3.1, pages 73-86, Theorem 3, Propositions 5-7.

# Verification Notes
- Definition source: direct from source pp. 73-78
- Confidence rationale: central construction, extensively developed
- Uncertainties: none
- Cross-reference status: verified
