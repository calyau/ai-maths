---
concept: Chinese Remainder Theorem
slug: chinese-remainder-theorem
category: ring-theory
subcategory: structure-theorems
tier: intermediate
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Introduction to Rings"
chapter_number: 7
pdf_page: 265
section: "7.6 The Chinese Remainder Theorem"
extraction_confidence: high
aliases:
  - "CRT"
prerequisites:
  - commutative-ring
  - ideal
  - quotient-ring
  - comaximal-ideals
extends: []
related:
  - direct-product-of-rings
  - comaximal-ideals
contrasts_with: []
answers_questions:
  - "What is the Chinese Remainder Theorem for rings?"
  - "When is a quotient ring isomorphic to a product of quotient rings?"
---

# Quick Definition
If $A_1, \ldots, A_k$ are pairwise comaximal ideals of a commutative ring R, then $R/(A_1 \cdots A_k) \cong R/A_1 \times \cdots \times R/A_k$.

# Core Definition
(Theorem 17) The map $R \to R/A_1 \times \cdots \times R/A_k$ defined by $r \mapsto (r+A_1, \ldots, r+A_k)$ is a ring homomorphism with kernel $A_1 \cap \cdots \cap A_k$. If the ideals $A_i$ and $A_j$ are comaximal for all $i \neq j$, then this map is surjective and $A_1 \cap \cdots \cap A_k = A_1 \cdots A_k$, giving $R/(A_1 A_2 \cdots A_k) \cong R/A_1 \times R/A_2 \times \cdots \times R/A_k$ (Dummit & Foote, pp. 265-267).

# Prerequisites
- **Commutative ring** — R is commutative with identity
- **Ideal** — The $A_i$ are ideals of R
- **Quotient ring** — The theorem produces quotient rings
- **Comaximal ideals** — The pairwise comaximal condition $A_i + A_j = R$

# Key Properties
1. The kernel of the natural map is $A_1 \cap \cdots \cap A_k$
2. Pairwise comaximality implies surjectivity
3. Pairwise comaximality implies $A_1 \cap \cdots \cap A_k = A_1 \cdots A_k$
4. Special case: $\mathbb{Z}/mn\mathbb{Z} \cong \mathbb{Z}/m\mathbb{Z} \times \mathbb{Z}/n\mathbb{Z}$ when $\gcd(m,n) = 1$ (p. 267)
5. Induces isomorphism on unit groups: $(\mathbb{Z}/mn\mathbb{Z})^{\times} \cong (\mathbb{Z}/m\mathbb{Z})^{\times} \times (\mathbb{Z}/n\mathbb{Z})^{\times}$ (p. 268)

# Construction / Recognition
## To Apply:
1. Identify ideals $A_1, \ldots, A_k$ in R
2. Verify pairwise comaximality: $A_i + A_j = R$ for $i \neq j$
3. Conclude $R/(A_1 \cdots A_k) \cong \prod R/A_i$

# Context & Application
The CRT originated from the problem of solving simultaneous congruences in $\mathbb{Z}$, considered by ancient Chinese mathematicians. The ring-theoretic version gives the multiplicativity of Euler's $\varphi$-function: $\varphi(mn) = \varphi(m)\varphi(n)$ when $\gcd(m,n) = 1$ (p. 268).

# Examples
**Example 1** (p. 267): $\mathbb{Z}/15\mathbb{Z} \cong \mathbb{Z}/3\mathbb{Z} \times \mathbb{Z}/5\mathbb{Z}$ since $\gcd(3,5) = 1$.

**Example 2** (p. 268): $\mathbb{Z}/n\mathbb{Z} \cong \mathbb{Z}/p_1^{\alpha_1}\mathbb{Z} \times \cdots \times \mathbb{Z}/p_k^{\alpha_k}\mathbb{Z}$ for $n = p_1^{\alpha_1} \cdots p_k^{\alpha_k}$ (Corollary 18).

# Relationships

## Related
- **direct-product-of-rings** — The CRT produces direct products
- **comaximal-ideals** — The key hypothesis

# Common Errors
- **Error**: Applying CRT without checking comaximality
  **Correction**: $\mathbb{Z}/4\mathbb{Z} \not\cong \mathbb{Z}/2\mathbb{Z} \times \mathbb{Z}/2\mathbb{Z}$ because $\gcd(2,2) \neq 1$

# Common Confusions
- **Confusion**: Thinking the CRT only applies to $\mathbb{Z}$
  **Clarification**: It applies to any commutative ring with pairwise comaximal ideals

# Source Reference
Chapter 7, Section 7.6, Theorem 17, pages 265-267. See Corollary 18, pages 268-269.

# Verification Notes
- Definition: Direct from Theorem 17, pp. 265-267
- Confidence: HIGH — fundamental theorem with complete proof
