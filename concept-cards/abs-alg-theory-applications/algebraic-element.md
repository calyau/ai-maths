---
# === CORE IDENTIFICATION ===
concept: Algebraic Element
slug: algebraic-element

# === CLASSIFICATION ===
category: field-theory
subcategory: field-extensions
tier: advanced

# === PROVENANCE ===
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Fields"
chapter_number: 21
pdf_page: 274
section: "21.1 Extension Fields"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "algebraic over F"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - extension-field
  - polynomial
extends: []
related:
  - minimal-polynomial
  - algebraic-extension
  - algebraic-number
contrasts_with:
  - transcendental-element

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What does it mean for an element to be algebraic over a field?"
  - "How do algebraic elements differ from transcendental elements?"
---

# Quick Definition

An element $\alpha$ in an extension field $E$ over $F$ is algebraic over $F$ if $f(\alpha) = 0$ for some nonzero polynomial $f(x) \in F[x]$.

# Core Definition

An element $\alpha$ in an extension field $E$ over $F$ is **algebraic** over $F$ if $f(\alpha) = 0$ for some nonzero polynomial $f(x) \in F[x]$ (Judson, p. 276).

# Prerequisites

- **Extension field** — Algebraic elements live in extension fields
- **Polynomial** — The definition involves polynomials over the base field

# Key Properties

1. If $\alpha$ is algebraic over $F$, there is a unique monic irreducible polynomial of smallest degree having $\alpha$ as a root (the minimal polynomial, Theorem 21.10)
2. $F(\alpha) \cong F[x]/\langle p(x) \rangle$ where $p(x)$ is the minimal polynomial (Proposition 21.12)
3. Every element of $F(\alpha)$ can be written uniquely as $b_0 + b_1\alpha + \cdots + b_{n-1}\alpha^{n-1}$ (Theorem 21.13)
4. Every element of a finite extension is algebraic (Theorem 21.15)

# Construction / Recognition

## To Recognize:
1. Given $\alpha \in E$, search for a nonzero polynomial $f(x) \in F[x]$ with $f(\alpha) = 0$
2. If found, $\alpha$ is algebraic; otherwise, $\alpha$ is transcendental

# Context & Application

The distinction between algebraic and transcendental elements is fundamental in field theory. Algebraic elements are "reachable" by polynomial equations over the base field, while transcendental elements are not. Most of Chapters 21-23 focus on algebraic extensions.

# Examples

**Example 1** (p. 276): $\sqrt{2}$ is algebraic over $\mathbb{Q}$ since it is a zero of $x^2 - 2 \in \mathbb{Q}[x]$.

**Example 2** (p. 276): $i$ is algebraic over $\mathbb{Q}$ since it is a zero of $x^2 + 1 \in \mathbb{Q}[x]$.

**Example 3** (p. 277): $\sqrt{2 + \sqrt{3}}$ is algebraic over $\mathbb{Q}$ since it is a zero of $x^4 - 4x^2 + 1$.

# Relationships

## Builds Upon
- **Extension field** — Algebraic elements are defined in extension fields

## Enables
- **Minimal polynomial** — Every algebraic element has one
- **Algebraic extension** — An extension where every element is algebraic
- **Simple extension** — $F(\alpha)$ is a finite extension when $\alpha$ is algebraic

## Contrasts With
- **Transcendental element** — An element that is not a root of any polynomial over $F$

# Common Errors

- **Error**: Assuming $\alpha$ is algebraic over $F$ because it is algebraic over some extension of $F$
  **Correction**: Algebraicity depends on the base field; $\pi$ is algebraic over $\mathbb{R}$ but transcendental over $\mathbb{Q}$

# Common Confusions

- **Confusion**: Thinking algebraic elements must be "nice" numbers like square roots
  **Clarification**: Any root of any polynomial over $F$ is algebraic, including roots of high-degree polynomials

# Source Reference

Chapter 21: Fields, Section 21.1, pages 276–278. See Theorems 21.10, 21.13, 21.15.

# Verification Notes

- Definition source: Direct from p. 276
- Confidence: HIGH — explicit definition
- Cross-reference status: Verified
- Uncertainties: None
