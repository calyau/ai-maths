---
concept: Extension of Scalars
slug: extension-of-scalars
category: module-theory
subcategory: tensor-products
tier: advanced
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Introduction to Module Theory"
chapter_number: 10
pdf_page: 365
section: "10.4 Tensor Products of Modules"
extraction_confidence: high
aliases:
  - "change of base"
  - "base change"
  - "scalar extension"
prerequisites:
  - tensor-product
  - left-module
extends: []
related:
  - restriction-of-scalars
contrasts_with:
  - restriction-of-scalars
answers_questions:
  - "What is extension of scalars?"
---

# Quick Definition
Extension of scalars converts an R-module N into an S-module $S \otimes_R N$ when there is a ring homomorphism $R \to S$, by tensoring with S.

# Core Definition
Let $f: R \to S$ be a ring homomorphism with $f(1_R) = 1_S$. For any left R-module N, the tensor product $S \otimes_R N$ is a left S-module called the module obtained by extension of scalars (or change of base) from R to S. The natural map $\iota: N \to S \otimes_R N$ defined by $n \mapsto 1 \otimes n$ is an R-module homomorphism but need not be injective (Dummit & Foote, pp. 365-369).

# Prerequisites
- **tensor-product** — Extension of scalars uses the tensor product construction
- **left-module** — We extend modules from one ring to another

# Key Properties
1. $S \otimes_R R^n \cong S^n$ — extending scalars for free modules preserves rank
2. The map $\iota: N \to S \otimes_R N$ given by $n \mapsto 1 \otimes n$ need not be injective
3. $\mathbb{Q} \otimes_{\mathbb{Z}} A = 0$ for any finite abelian group A (torsion elements are killed)
4. Universal property: any R-module map from N to an S-module factors through $S \otimes_R N$

# Examples
**Example 1** (p. 371): $\mathbb{Q} \otimes_{\mathbb{Z}} \mathbb{Z}^n \cong \mathbb{Q}^n$ — extending scalars from $\mathbb{Z}$ to $\mathbb{Q}$.
**Example 2** (p. 371): $\mathbb{Q} \otimes_{\mathbb{Z}} A = 0$ for any finite abelian group A.

# Relationships
## Builds Upon
- **tensor-product**

## Enables
- **flat-module** — Flatness measures when extension of scalars preserves injections

## Contrasts With
- **restriction-of-scalars** — The reverse operation: forgetting part of the module structure

# Source Reference
Chapter 10, Section 10.4, pp. 365-371.

# Verification Notes
- Confidence: HIGH — extensively developed with examples
