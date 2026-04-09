---
# === CORE IDENTIFICATION ===
concept: Weyl Character Formula
slug: weyl-character-formula

# === CLASSIFICATION ===
category: representations
subcategory: highest-weight-theory
tier: advanced

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Representations of Semisimple Lie Algebras"
chapter_number: 9
pdf_page: 116
section: "9.5 Characters and Weyl character formula"

# === CONFIDENCE ===
extraction_confidence: medium

# === VARIANTS (authority control) ===
aliases:
  - "Weyl formula"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - character-of-representation
  - irreducible-highest-weight-module
  - dominant-integral-weight
  - weyl-group
  - bgg-resolution
extends: []
related:
  - weyl-dimension-formula
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the Weyl character formula?"
  - "What must I know before understanding the Weyl character formula?"
---

# Quick Definition
The Weyl character formula gives a closed-form expression for the character of the irreducible finite-dimensional representation $L_\lambda$ in terms of the Weyl group and the half-sum of positive roots $\rho$.

# Core Definition
(Kirillov, Section 9.5, p. 116): The Weyl character formula states:

$$\mathrm{ch}(L_\lambda) = \frac{\sum_{w \in W} (-1)^{\ell(w)} e^{w(\lambda + \rho)}}{\sum_{w \in W} (-1)^{\ell(w)} e^{w(\rho)}} = \frac{\sum_{w \in W} (-1)^{\ell(w)} e^{w(\lambda + \rho)}}{\prod_{\alpha \in R_+} (e^{\alpha/2} - e^{-\alpha/2})}$$

where $\rho = \frac{1}{2}\sum_{\alpha \in R_+} \alpha$, $\ell(w)$ is the length of the Weyl group element, and $\lambda \in P_+$.

# Prerequisites
- **Character of a representation** -- the formula computes the character
- **Irreducible highest-weight module** -- $L_\lambda$ is the module whose character is computed
- **Dominant integral weight** -- the formula applies for $\lambda \in P_+$
- **Weyl group** -- the sum runs over $W$
- **BGG resolution** -- provides one route to proving the formula

# Key Properties
1. The denominator (Weyl denominator) equals $\prod_{\alpha \in R_+}(e^{\alpha/2} - e^{-\alpha/2})$
2. Setting $\lambda = 0$ gives the Weyl denominator identity: $\sum_{w \in W} (-1)^{\ell(w)} e^{w\rho} = e^\rho \prod_{\alpha \in R_+}(1 - e^{-\alpha})$
3. Evaluating at the identity (via L'Hopital) gives the Weyl dimension formula
4. The formula can be derived from the BGG resolution via Euler characteristic
5. The alternating sum over the Weyl group implements inclusion-exclusion

# Context & Application
The Weyl character formula is the culminating result of the representation theory developed in this book. It provides a complete answer to the question of weight multiplicities for irreducible representations. Combined with the decomposition of arbitrary representations into irreducibles, it gives complete information about the representation theory of semisimple Lie algebras.

# Examples
**Example**: For $\mathfrak{sl}(2, \mathbb{C})$ with $\lambda = n$, the Weyl character formula gives:

$$\mathrm{ch}(L_n) = \frac{e^{n+1} - e^{-(n+1)}}{e - e^{-1}} = e^n + e^{n-2} + \cdots + e^{-n}$$

recovering the known character of the $(n+1)$-dimensional irreducible.

# Relationships
## Builds Upon
- **Character of a representation** -- the formula computes characters
- **BGG resolution** -- one proof method
- **Weyl group** -- the sum is over $W$

## Enables
- **Weyl dimension formula** -- obtained by specialization
- **Weight multiplicity computations** -- by expanding the formula

# Common Errors
- **Error**: Forgetting the $\rho$-shift: using $w(\lambda)$ instead of $w(\lambda + \rho)$
  **Correction**: The formula involves $w(\lambda + \rho)$, not $w(\lambda)$

# Common Confusions
- **Confusion**: Thinking the formula directly gives individual weight multiplicities
  **Clarification**: The formula gives the entire character as a formal sum; extracting individual multiplicities requires expanding the ratio, which can be non-trivial

# Source Reference
Chapter 9, Section 9.5 "Characters and Weyl character formula," p. 116.

# Verification Notes
- Definition source: Synthesized -- Section 9.5 is listed but content is truncated in the source markdown; formula stated from standard references consistent with this text
- Confidence rationale: Medium -- the section heading confirms the topic but detailed content is truncated
- Uncertainties: Exact notation used by Kirillov not verified from truncated section
- Cross-reference status: Verified against standard references
