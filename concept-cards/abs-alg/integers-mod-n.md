---
concept: "Integers Modulo n"
slug: integers-mod-n
category: foundations
subcategory: modular-arithmetic
tier: foundational
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Preliminaries"
chapter_number: 0
pdf_page: 14
section: "0.3 The Integers Modulo n"
extraction_confidence: high
aliases:
  - "$\\mathbb{Z}/n\\mathbb{Z}$"
  - "residue classes mod n"
prerequisites:
  - congruence-mod-n
extends:
  - congruence-mod-n
related:
  - cyclic-group
  - abelian-group
  - quotient-group
contrasts_with: []
answers_questions:
  - "What is the group $\\mathbb{Z}/n\\mathbb{Z}$?"
  - "What is modular arithmetic?"
---

# Quick Definition
$\mathbb{Z}/n\mathbb{Z}$ is the set of n residue classes $\{\bar{0}, \bar{1}, \ldots, \overline{n-1}\}$ with well-defined addition and multiplication. Under addition, it is a cyclic group of order n. The subset $(\mathbb{Z}/n\mathbb{Z})^\times$ of invertible classes forms a group under multiplication.

# Core Definition
The set $\mathbb{Z}/n\mathbb{Z} = \{\bar{0}, \bar{1}, \ldots, \overline{n-1}\}$ of residue classes modulo n has well-defined addition $\bar{a} + \bar{b} = \overline{a+b}$ and multiplication $\bar{a} \cdot \bar{b} = \overline{ab}$ (Theorem 3). Under addition, $\mathbb{Z}/n\mathbb{Z}$ is an abelian group with identity $\bar{0}$. The subset $(\mathbb{Z}/n\mathbb{Z})^\times = \{\bar{a} \mid (a,n) = 1\}$ is an abelian group under multiplication of order $\varphi(n)$ (Proposition 4) (Dummit & Foote, pp. 7-10).

# Prerequisites
- **Congruence modulo n** — $\mathbb{Z}/n\mathbb{Z}$ consists of congruence classes

# Key Properties
1. $|\mathbb{Z}/n\mathbb{Z}| = n$ under addition
2. $\mathbb{Z}/n\mathbb{Z}$ is the prototypical cyclic group of order n
3. $|(\mathbb{Z}/n\mathbb{Z})^\times| = \varphi(n)$
4. $\bar{a}$ is invertible mod n iff $(a,n) = 1$
5. The Euclidean Algorithm computes multiplicative inverses in $(\mathbb{Z}/n\mathbb{Z})^\times$

# Context & Application
$\mathbb{Z}/n\mathbb{Z}$ is the first example of a quotient group encountered in the text. It motivates the general quotient group construction, as addition of residue classes by representatives foreshadows coset multiplication.

# Examples
**Example 1** (p. 8): $\mathbb{Z}/12\mathbb{Z}$: $\bar{5} + \bar{8} = \bar{1}$, $\bar{5} \cdot \bar{8} = \bar{4}$.
**Example 2** (p. 10): $(\mathbb{Z}/9\mathbb{Z})^\times = \{\bar{1}, \bar{2}, \bar{4}, \bar{5}, \bar{7}, \bar{8}\}$.

# Relationships
## Builds Upon
- **congruence-mod-n**

## Enables
- **cyclic-group** — $\mathbb{Z}/n\mathbb{Z} \cong Z_n$
- **quotient-group** — $\mathbb{Z}/n\mathbb{Z}$ is a quotient of $\mathbb{Z}$ by $n\mathbb{Z}$

## Related
- **abelian-group** — $\mathbb{Z}/n\mathbb{Z}$ and $(\mathbb{Z}/n\mathbb{Z})^\times$ are abelian

# Source Reference
Chapter 0, Section 0.3, pages 7-11, Theorem 3, Proposition 4.

# Verification Notes
- Definition source: direct from source pp. 7-9
- Confidence rationale: extensively developed
- Uncertainties: none
- Cross-reference status: verified
