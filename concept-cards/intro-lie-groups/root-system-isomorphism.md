---
# === CORE IDENTIFICATION ===
concept: Root System Isomorphism
slug: root-system-isomorphism

# === CLASSIFICATION ===
category: root-systems
subcategory: weyl-group
tier: intermediate

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Root Systems"
chapter_number: 8
pdf_page: 92
section: "8.2. Automorphisms and Weyl group"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "isomorphism of root systems"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - abstract-root-system
extends: []
related:
  - weyl-group
  - dynkin-diagram
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "When are two root systems isomorphic?"
  - "Does a root system isomorphism preserve the inner product?"
---

# Quick Definition
An isomorphism of root systems $R_1 \subset E_1$ and $R_2 \subset E_2$ is a vector space isomorphism $\varphi: E_1 \to E_2$ that bijects $R_1$ onto $R_2$ and preserves all integers $n_{\alpha\beta}$. It need not preserve inner products.

# Core Definition
An isomorphism $\varphi: R_1 \to R_2$ is a vector space isomorphism $\varphi: E_1 \to E_2$ which gives a bijection $R_1 \xrightarrow{\sim} R_2$ and satisfies $n_{\varphi(\alpha)\varphi(\beta)} = n_{\alpha\beta}$ for any $\alpha, \beta \in R_1$ (Definition 8.5, p. 92).

# Prerequisites
- **abstract-root-system** -- isomorphisms are defined between root systems

# Key Properties
1. Preserves all integers $n_{\alpha\beta}$ (and hence the Cartan matrix, if simple roots are compatible)
2. Need not preserve the inner product: $R$ and $cR$ are isomorphic for any $c > 0$ (p. 92)
3. Inner-product-preserving maps are automatically isomorphisms, but the converse is false
4. The Dynkin diagram determines a root system up to isomorphism (Theorem 8.48(3))

# Construction / Recognition
To check that $\varphi$ is an isomorphism:
1. Verify $\varphi$ is a linear isomorphism $E_1 \to E_2$
2. Verify $\varphi(R_1) = R_2$
3. For all $\alpha,\beta \in R_1$, verify $n_{\varphi(\alpha)\varphi(\beta)} = n_{\alpha\beta}$

# Context & Application
Root system isomorphism is the correct equivalence relation for classifying root systems. Because it preserves the integers $n_{\alpha\beta}$ rather than the inner product itself, rescaled root systems are considered equivalent. The classification theorem (Theorem 8.49) classifies root systems up to this notion of isomorphism.

# Examples
**Example** (p. 92): For any $c \in \mathbb{R}_+$, the map $v \mapsto cv$ gives an isomorphism $R \xrightarrow{\sim} cR$. This does not preserve the inner product (it scales it by $c^2$), but it preserves all $n_{\alpha\beta}$.

# Relationships
## Builds Upon
- **abstract-root-system**

## Enables
- **dynkin-diagram** -- classifies root systems up to isomorphism

## Related
- **weyl-group** -- Weyl group elements are special automorphisms

## Contrasts With
(none)

# Common Errors
- **Error**: Requiring isomorphisms to preserve the inner product
  **Correction**: Only the integers $n_{\alpha\beta}$ must be preserved, not the inner product itself

# Common Confusions
- **Confusion**: Thinking every automorphism of a root system is a Weyl group element
  **Clarification**: The Weyl group is a (usually proper) subgroup of $\mathrm{Aut}(R)$

# Source Reference
Chapter 8: Root Systems, Section 8.2, page 92. Definition 8.5.

# Verification Notes
- Definition source: Direct from Definition 8.5
- Confidence rationale: HIGH -- explicit definition
- Uncertainties: None
- Cross-reference status: Verified
