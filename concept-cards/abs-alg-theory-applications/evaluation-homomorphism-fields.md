---
# === CORE IDENTIFICATION ===
concept: Evaluation Homomorphism for Fields
slug: evaluation-homomorphism-fields

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
  - "substitution homomorphism"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - extension-field
  - ring-homomorphism
extends: []
related:
  - minimal-polynomial
  - algebraic-element
  - transcendental-element
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the evaluation homomorphism and why is it important for field extensions?"
---

# Quick Definition

The evaluation homomorphism $\phi_\alpha: F[x] \to E$ sends $p(x)$ to $p(\alpha)$ for a fixed $\alpha \in E$. Its kernel determines whether $\alpha$ is algebraic or transcendental over $F$.

# Core Definition

Let $E$ be an extension of $F$ and $\alpha \in E$. The **evaluation homomorphism** $\phi_\alpha: F[x] \to E$ is defined by $\phi_\alpha(p(x)) = p(\alpha)$ (Judson, pp. 276–277).

- If $\ker \phi_\alpha = \{0\}$, then $\alpha$ is transcendental and $F(\alpha) \cong F(x)$ (Theorem 21.9)
- If $\ker \phi_\alpha = \langle p(x) \rangle \neq \{0\}$, then $\alpha$ is algebraic with minimal polynomial $p(x)$ and $F(\alpha) \cong F[x]/\langle p(x) \rangle$ (Proposition 21.12)

# Prerequisites

- **Extension field** — The homomorphism maps into an extension
- **Ring homomorphism** — The evaluation map is a ring homomorphism

# Key Properties

1. The kernel determines algebraicity: trivial kernel means transcendental
2. The kernel is always a principal ideal $\langle p(x) \rangle$ since $F[x]$ is a PID
3. The image is $F[\alpha] \cong F[x]/\ker\phi_\alpha$
4. For algebraic $\alpha$, the image equals $F(\alpha)$

# Context & Application

The evaluation homomorphism is the fundamental tool connecting polynomials to field extensions. It translates the abstract question "is $\alpha$ algebraic?" into the concrete question "is $\ker \phi_\alpha$ trivial?"

# Examples

**Example 1**: For $\alpha = \sqrt{2} \in \mathbb{R}$, $\phi_\alpha: \mathbb{Q}[x] \to \mathbb{R}$ has $\ker \phi_\alpha = \langle x^2 - 2 \rangle$.

**Example 2**: For $\alpha = \pi \in \mathbb{R}$, $\phi_\alpha: \mathbb{Q}[x] \to \mathbb{R}$ has $\ker \phi_\alpha = \{0\}$ (since $\pi$ is transcendental).

# Relationships

## Related
- **Minimal polynomial** — The generator of $\ker \phi_\alpha$
- **Algebraic element** — $\alpha$ is algebraic iff $\ker \phi_\alpha \neq \{0\}$
- **Transcendental element** — $\alpha$ is transcendental iff $\ker \phi_\alpha = \{0\}$

# Source Reference

Chapter 21: Fields, Section 21.1, pages 276–278. Theorems 21.9, 21.10, Proposition 21.12.

# Verification Notes

- Definition source: Synthesized from pp. 276–278
- Confidence: HIGH — central construction in the chapter
- Cross-reference status: Verified
- Uncertainties: None
