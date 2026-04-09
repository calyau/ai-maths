---
# === CORE IDENTIFICATION ===
concept: Constructible Number
slug: constructible-number

# === CLASSIFICATION ===
category: field-theory
subcategory: geometric-constructions
tier: advanced

# === PROVENANCE ===
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Fields"
chapter_number: 21
pdf_page: 274
section: "21.3 Geometric Constructions"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - extension-field
  - degree-of-field-extension
extends: []
related:
  - doubling-the-cube
  - squaring-the-circle
  - trisecting-an-angle
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a constructible number?"
  - "What is the algebraic characterization of constructible numbers?"
---

# Quick Definition

A real number $\alpha$ is constructible if a line segment of length $|\alpha|$ can be constructed in a finite number of steps from a unit segment using only a straightedge and compass. The constructible numbers form a field.

# Core Definition

A real number $\alpha$ is **constructible** if we can construct a line segment of length $|\alpha|$ in a finite number of steps from a segment of unit length by using a straightedge and compass (Judson, p. 285).

**Algebraic characterization (Theorem 21.43):** $\alpha$ is constructible if and only if there exists a sequence of fields $\mathbb{Q} = F_0 \subset F_1 \subset \cdots \subset F_k$ such that $F_i = F_{i-1}(\sqrt{\alpha_i})$ with $\alpha_i \in F_i$ and $\alpha \in F_k$. In particular, $[\mathbb{Q}(\alpha):\mathbb{Q}] = 2^k$ for some integer $k > 0$.

# Prerequisites

- **Extension field** — Constructible numbers are characterized via field extensions
- **Degree of field extension** — The degree must be a power of 2

# Key Properties

1. The set of all constructible numbers forms a subfield of $\mathbb{R}$ (Theorem 21.37)
2. If $\alpha$ is constructible, then $\sqrt{\alpha}$ is constructible (Lemma 21.39)
3. $\alpha$ is constructible implies $[\mathbb{Q}(\alpha):\mathbb{Q}]$ is a power of 2 (Theorem 21.43)
4. The field of constructible numbers is an algebraic extension of $\mathbb{Q}$ (Corollary 21.44)
5. Each step of construction involves solving at most a quadratic equation

# Construction / Recognition

## To Determine if Constructible:
1. Find the minimal polynomial of $\alpha$ over $\mathbb{Q}$
2. Compute $[\mathbb{Q}(\alpha):\mathbb{Q}]$
3. If this degree is not a power of 2, $\alpha$ is not constructible
4. If it is a power of 2, further analysis may be needed

# Context & Application

This concept connects abstract algebra to classical Greek geometry problems. The algebraic characterization provides a powerful tool for proving impossibility results: if $[\mathbb{Q}(\alpha):\mathbb{Q}]$ is not a power of 2, then $\alpha$ cannot be constructed.

# Examples

**Example 1** (p. 287): $\sqrt[3]{2}$ is not constructible because $[\mathbb{Q}(\sqrt[3]{2}):\mathbb{Q}] = 3$, which is not a power of 2. This proves the impossibility of doubling the cube.

**Example 2** (p. 288): $\cos 20°$ is not constructible because its minimal polynomial $8x^3 - 6x - 1$ has degree 3. This proves a $60°$ angle cannot be trisected.

# Relationships

## Builds Upon
- **Extension field** — Constructibility is characterized by field extension towers
- **Degree of field extension** — Must be a power of 2

## Enables
- **Doubling the cube** — Proved impossible via constructible numbers
- **Trisecting an angle** — Proved impossible via constructible numbers
- **Squaring the circle** — Proved impossible via transcendence

# Source Reference

Chapter 21: Fields, Section 21.3 "Geometric Constructions," pages 285–288. See Theorems 21.37, 21.43.

# Verification Notes

- Definition source: Direct from p. 285
- Confidence: HIGH — explicit definition with algebraic characterization
- Cross-reference status: Verified
- Uncertainties: None
