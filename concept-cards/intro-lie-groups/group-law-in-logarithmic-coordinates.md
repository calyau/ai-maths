---
# === CORE IDENTIFICATION ===
concept: Group Law in Logarithmic Coordinates
slug: group-law-in-logarithmic-coordinates

# === CLASSIFICATION ===
category: lie-algebras
subcategory: exponential-map
tier: intermediate

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Lie Groups and Lie Algebras"
chapter_number: 3
pdf_page: 23
section: "3.2"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "$\\mu(x, y)$"
  - "logarithmic coordinates"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - exponential-map
extends: []
related:
  - commutator-bracket
  - campbell-hausdorff-formula
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I use the exponential map to go between Lie group and Lie algebra?"
---

# Quick Definition

For small $x, y \in \mathfrak{g}$, the product $\exp(x)\exp(y)$ can be written as $\exp(\mu(x, y))$ where $\mu(x, y) = x + y + \frac{1}{2}[x, y] + \cdots$ is the group law expressed in logarithmic coordinates.

# Core Definition

(Kirillov, p. 22-23): For sufficiently small $x, y \in \mathfrak{g}$, the product $\exp(x)\exp(y)$ is close to $1 \in G$ and can be written as $\exp(\mu(x, y))$ for a smooth map $\mu: \mathfrak{g} \times \mathfrak{g} \to \mathfrak{g}$.

**Lemma 3.11**: $\mu(x, y) = x + y + \lambda(x, y) + \cdots$ where $\lambda$ is bilinear and skew-symmetric. Defining $[x, y] = 2\lambda(x, y)$: $\mu(x, y) = x + y + \frac{1}{2}[x, y] + \cdots$ (equation 3.2).

# Prerequisites

- **Exponential map** — provides the local coordinates

# Key Properties

1. $\mu(x, 0) = x$ and $\mu(0, y) = y$.
2. The first non-trivial term is $\frac{1}{2}[x, y]$ (bilinear, skew-symmetric).
3. Skew-symmetry of $\lambda$ follows from $\mu(x, x) = 2x$ (since $\exp(x)\exp(x) = \exp(2x)$).
4. The full series is the Campbell-Hausdorff formula (Theorem 3.34).

# Construction / Recognition

## To Construct/Create:
1. Use the exponential map to identify a neighborhood of $1 \in G$ with a neighborhood of $0 \in \mathfrak{g}$.
2. Express the group multiplication in these coordinates.

## To Identify/Recognize:
1. The expression for group multiplication written in terms of Lie algebra elements via the log map.

# Context & Application

Logarithmic coordinates are the natural coordinates near the identity. The group law in these coordinates encodes all the structure of the Lie group, and the lowest-order non-trivial term defines the Lie bracket.

# Examples

**Example** (p. 23): For an abelian group: $\mu(x, y) = x + y$ (all higher terms vanish).

**Example** (equation 3.3): The group commutator: $\exp(x)\exp(y)\exp(-x)\exp(-y) = \exp([x, y] + \cdots)$.

# Relationships

## Builds Upon
- **Exponential map** — provides the coordinate system

## Enables
- **Commutator bracket** — defined as twice the bilinear term
- **Campbell-Hausdorff formula** — the full series for $\mu$

# Common Errors

- **Error**: Assuming $\mu(x, y) = x + y$ always.
  **Correction**: This holds only for abelian groups. In general, $\mu(x, y) = x + y + \frac{1}{2}[x,y] + \cdots$.

# Common Confusions

- **Confusion**: Whether "logarithmic coordinates" are a global coordinate system.
  **Clarification**: No, they are only local (near $1 \in G$), since the exponential map is only a local diffeomorphism.

# Source Reference

Chapter 3: Lie Groups and Lie Algebras, Section 3.2, Lemma 3.11, equation (3.2), pages 22-23.

# Verification Notes

- Definition source: Direct from Lemma 3.11 and equation (3.2)
- Confidence rationale: Explicit formulas
- Uncertainties: None
- Cross-reference status: Verified with Theorem 3.34
