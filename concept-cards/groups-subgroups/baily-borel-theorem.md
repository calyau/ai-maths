---
# === CORE IDENTIFICATION ===
concept: Baily-Borel Theorem
slug: baily-borel-theorem

# === CLASSIFICATION ===
category: arithmetic-groups
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "Arithmetic Subgroups"
chapter_number: 7
pdf_page: 411
section: "Shimura varieties"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - Baily-Borel compactification
  - algebraization theorem

# === TYPED RELATIONSHIPS ===
prerequisites:
  - hermitian-symmetric-domain
  - torsion-free-arithmetic-group
extends: []
related:
  - connected-shimura-variety
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a Shimura variety?"
---

# Quick Definition

The Baily-Borel theorem states that for a torsion-free arithmetic subgroup $\Gamma$ of a simply connected semisimple group $G$ over $\mathbb{Q}$ (with no compact factors), the quotient $\Gamma \backslash X$ of the associated hermitian symmetric domain has a unique algebraic variety structure compatible with its complex structure.

# Core Definition

Theorem 16.2 (Milne, p. 411): Let $G$ be a simply connected semisimple algebraic group over $\mathbb{Q}$ having no simple factor $H$ with $H(\mathbb{R})$ compact. Let $u: U_1 \to G^{\mathrm{ad}}(\mathbb{R})$ satisfy conditions (a) and (b) of Theorem 16.1, and let $X = G^{\mathrm{ad}}(\mathbb{R})^+/K$. For each torsion-free arithmetic subgroup $\Gamma$ of $G(\mathbb{Q})$, $\Gamma \backslash X$ has a unique structure of an algebraic variety compatible with its complex structure.

# Prerequisites

- **Hermitian symmetric domain** — the space $X$ being quotiented
- **Torsion-free arithmetic group** — needed for smooth quotient

# Key Properties

1. The algebraic structure on $\Gamma \backslash X$ is unique given the complex structure
2. Torsion-freeness is needed for the quotient to be a manifold (not just an orbifold)
3. The compact factor exclusion ensures $X$ is noncompact
4. The theorem was strengthened by Borel to include certain non-torsion-free quotients

# Construction / Recognition

## To Apply:
1. Start with $G$ simply connected semisimple over $\mathbb{Q}$, no compact factors at infinity
2. Choose $u: U_1 \to G^{\mathrm{ad}}(\mathbb{R})$ satisfying Shimura conditions
3. Form $X = G^{\mathrm{ad}}(\mathbb{R})^+/K$
4. Choose a torsion-free arithmetic $\Gamma$ (exists by Theorem 8.1)
5. $\Gamma \backslash X$ is an algebraic variety

# Context & Application

The Baily-Borel theorem is the bridge between the analytic theory of locally symmetric spaces and algebraic geometry. It shows that the quotient spaces arising from arithmetic groups are not merely complex manifolds but algebraic varieties, enabling the use of algebraic geometry tools.

# Examples

**Example 1** (p. 411): For $G = \mathrm{SL}_2$ and $X = \mathcal{H}$, the quotients $\Gamma \backslash \mathcal{H}$ for torsion-free $\Gamma$ are algebraic curves (modular curves).

# Relationships

## Builds Upon
- **Hermitian symmetric domain** — the space being quotiented
- **Torsion-free arithmetic group** — ensures smooth quotient

## Enables
- **Connected Shimura variety** — the Baily-Borel theorem gives the algebraic structure

# Common Errors

- **Error**: Applying the theorem without excluding compact factors
  **Correction**: If $H(\mathbb{R})$ is compact for a simple factor $H$, the theorem does not apply directly

# Common Confusions

- **Confusion**: Thinking the algebraic structure depends on $\Gamma$
  **Clarification**: The algebraic structure is unique given the complex structure; different $\Gamma$ give different algebraic varieties but the algebraization is canonical

# Source Reference

Chapter VII: Arithmetic Subgroups, Section 16, page 411. Theorem 16.2.

# Verification Notes

- Definition source: Theorem 16.2 directly from p. 411
- Confidence: HIGH — explicit theorem statement
- Uncertainties: Proof references Milne 2005
- Cross-reference status: Verified
