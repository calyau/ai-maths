---
concept: Natural Projection
slug: natural-projection
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
  - "canonical projection"
  - "natural homomorphism"
  - "$\\pi$"
prerequisites:
  - quotient-group
  - normal-subgroup
extends:
  - homomorphism
related:
  - kernel
  - first-isomorphism-theorem
contrasts_with: []
answers_questions:
  - "What is the natural projection homomorphism?"
---

# Quick Definition
The natural projection $\pi: G \to G/N$ defined by $\pi(g) = gN$ is a surjective homomorphism with kernel N. It realizes every normal subgroup as a kernel.

# Core Definition
Let $N \trianglelefteq G$. The *natural projection* (or *canonical projection*) $\pi: G \to G/N$ defined by $\pi(g) = gN$ is a surjective homomorphism with $\ker\pi = N$. This proves that every normal subgroup is the kernel of some homomorphism (Proposition 7). A homomorphism $\Phi: G \to H$ *factors through* N if $N \leq \ker\Phi$, giving an induced homomorphism $\varphi: G/N \to H$ (Dummit & Foote, pp. 84-85, 101).

# Prerequisites
- **Quotient group**, **Normal subgroup**

# Key Properties
1. $\pi$ is surjective
2. $\ker\pi = N$
3. Every normal subgroup is the kernel of its natural projection
4. A homomorphism $\Phi: G \to H$ factors through N iff $N \leq \ker\Phi$

# Context & Application
The natural projection is the canonical way to produce a homomorphism from a normal subgroup. It converts the study of quotient groups into the study of homomorphisms.

# Examples
**Example 1** (p. 73): $\pi: \mathbb{Z} \to \mathbb{Z}/n\mathbb{Z}$ by $a \mapsto \bar{a}$ is the natural projection with kernel $n\mathbb{Z}$.

# Relationships
## Builds Upon
- **quotient-group**, **normal-subgroup**

## Related
- **kernel** — $\ker\pi = N$
- **first-isomorphism-theorem** — connects images to quotients

# Source Reference
Chapter 3, Section 3.1, pages 84-85.

# Verification Notes
- Definition source: direct from source pp. 84-85
- Confidence rationale: explicitly defined
- Uncertainties: none
- Cross-reference status: verified
