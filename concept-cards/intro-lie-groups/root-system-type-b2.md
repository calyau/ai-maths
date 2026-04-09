---
# === CORE IDENTIFICATION ===
concept: Root System Type B2
slug: root-system-type-b2

# === CLASSIFICATION ===
category: root-systems
subcategory: abstract-root-systems
tier: intermediate

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Root Systems"
chapter_number: 8
pdf_page: 93
section: "8.3. Pairs of roots and rank two root systems"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "$B_2$"
  - "$C_2$"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - abstract-root-system
  - rank-two-root-system-classification
extends: []
related:
  - root-system-type-a
  - root-system-type-g2
  - long-and-short-roots
contrasts_with:
  - root-system-type-a
  - root-system-type-g2

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the $B_2$ root system?"
---

# Quick Definition
$B_2$ is the rank two root system with 8 roots and two root lengths in ratio $\sqrt{2}$, with maximal angle $3\pi/4$ between roots. It is also denoted $C_2$ ($B_2 = C_2$).

# Core Definition
$B_2$ is one of the four rank two reduced root systems (Theorem 8.10, p. 93). It has 8 roots, with long roots at angles $\pi/2$ and short roots at angles $\pi/2$, and the maximal angle between a long and a short root is $3\pi/4$. The ratio of long to short root lengths is $\sqrt{2}$. The Dynkin diagram is two vertices connected by a double edge with an arrow.

# Prerequisites
- **abstract-root-system** -- $B_2$ is a root system
- **rank-two-root-system-classification** -- $B_2$ is one of the four rank two types

# Key Properties
1. 8 roots total: 4 long roots and 4 short roots
2. Length ratio: $|\alpha_{\text{long}}|/|\alpha_{\text{short}}| = \sqrt{2}$
3. Maximal angle between non-proportional roots: $3\pi/4$
4. $B_2 = C_2$ (Remark 8.50, p. 106)
5. Dynkin diagram: double edge with arrow

# Construction / Recognition
In $\mathbb{R}^2$ with standard basis $e_1, e_2$:
- Long roots: $\pm e_1 \pm e_2$ (length $\sqrt{2}$)
- Short roots: $\pm e_1, \pm e_2$ (length 1)

# Context & Application
$B_2$ is the simplest non-simply-laced root system. It corresponds to the double edge in a Dynkin diagram and generalizes to the $B_n$ and $C_n$ series. The distinction between $B_n$ and $C_n$ for $n \geq 3$ involves which roots (long or short) form the simple roots, but for $n = 2$ they coincide.

# Examples
**Example** (p. 93): $B_2$ is shown in Figure 8.1 as one of the four rank two root systems. The angle and length ratio match case (3a)/(3b) of Theorem 8.9.

# Relationships
## Builds Upon
- **rank-two-root-system-classification**

## Enables
- **dynkin-diagram** -- the double edge corresponds to $B_2$

## Related
- **long-and-short-roots** -- $B_2$ has two root lengths

## Contrasts With
- **root-system-type-a** -- simply laced (all roots equal length)
- **root-system-type-g2** -- triple edge, length ratio $\sqrt{3}$

# Common Errors
- **Error**: Distinguishing $B_2$ and $C_2$ as different root systems
  **Correction**: $B_2 = C_2$; they only differ for $n \geq 3$

# Common Confusions
(none)

# Source Reference
Chapter 8: Root Systems, Section 8.3, pages 93--94. Theorem 8.10, Figure 8.1. Also Remark 8.50.

# Verification Notes
- Definition source: Direct from Theorem 8.10
- Confidence rationale: HIGH -- explicit in classification
- Uncertainties: None
- Cross-reference status: Verified
