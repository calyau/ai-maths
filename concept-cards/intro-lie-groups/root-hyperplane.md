---
# === CORE IDENTIFICATION ===
concept: Root Hyperplane
slug: root-hyperplane

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
pdf_page: 98
section: "8.6. Weyl chambers"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "$L_\\alpha$"
  - "hyperplane orthogonal to a root"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - abstract-root-system
extends: []
related:
  - reflection-in-root-system
  - weyl-chamber
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a root hyperplane?"
---

# Quick Definition
The root hyperplane $L_\alpha$ is the hyperplane in $E$ orthogonal to the root $\alpha$: $L_\alpha = \{\lambda \in E \mid (\alpha,\lambda) = 0\}$. It is the fixed-point set of the reflection $s_\alpha$.

# Core Definition
For a root $\alpha \in R$, the root hyperplane is (equation 8.3, p. 90; equation 8.15, p. 98):

$$L_\alpha = \{\lambda \in E \mid (\alpha,\lambda) = 0\}$$

The reflection $s_\alpha$ fixes $L_\alpha$ pointwise and sends $\alpha$ to $-\alpha$.

# Prerequisites
- **abstract-root-system** -- root hyperplanes are associated to roots

# Key Properties
1. $L_\alpha = L_{-\alpha}$ (the hyperplane depends only on the direction of $\alpha$)
2. $L_\alpha$ is the fixed-point set of $s_\alpha$
3. The complement $E \setminus \bigcup_{\alpha \in R} L_\alpha$ decomposes into Weyl chambers
4. $w(L_\alpha) = L_{w(\alpha)}$ for $w \in W$ (Lemma 8.7)
5. Walls of the positive Weyl chamber are $L_{\alpha_i}$ for simple roots $\alpha_i$ (Corollary 8.28)

# Construction / Recognition
Given $\alpha \in R$, the hyperplane $L_\alpha = \ker(\alpha, \cdot) = \{\lambda \mid (\alpha,\lambda) = 0\}$.

# Context & Application
Root hyperplanes partition $E$ into Weyl chambers. The number of root hyperplanes separating two Weyl chambers defines the Weyl length function. Adjacent Weyl chambers share a wall (a codimension-one face lying in some $L_\alpha$).

# Examples
**Example** (p. 98): For $A_2$, there are 3 root hyperplanes (one per pair $\pm\alpha$), dividing $E \cong \mathbb{R}^2$ into 6 Weyl chambers (Figure 8.4).

# Relationships
## Builds Upon
- **abstract-root-system**

## Enables
- **weyl-chamber** -- defined as connected components of complement to root hyperplanes

## Related
- **reflection-in-root-system** -- $s_\alpha$ is the reflection across $L_\alpha$

## Contrasts With
(none)

# Common Errors
(none)

# Common Confusions
(none)

# Source Reference
Chapter 8: Root Systems, Sections 8.1 and 8.6, pages 90, 98. Equations (8.3), (8.15).

# Verification Notes
- Definition source: Direct from equations (8.3) and (8.15)
- Confidence rationale: HIGH -- explicit formula
- Uncertainties: None
- Cross-reference status: Verified
