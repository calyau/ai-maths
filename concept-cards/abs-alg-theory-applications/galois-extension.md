---
# === CORE IDENTIFICATION ===
concept: Galois Extension
slug: galois-extension

# === CLASSIFICATION ===
category: galois-theory
subcategory: field-automorphisms
tier: advanced

# === PROVENANCE ===
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Galois Theory"
chapter_number: 23
pdf_page: 307
section: "23.2 The Fundamental Theorem"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "Galois field extension"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - normal-extension
  - separable-extension
  - extension-field
extends:
  - extension-field
related:
  - fundamental-theorem-of-galois-theory
  - galois-group
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a Galois extension?"
  - "What conditions make an extension Galois?"
---

# Quick Definition

A field extension $E/F$ is a Galois extension if it is finite, normal, and separable. Equivalently, $E$ is the splitting field of a separable polynomial over $F$, or $F = E_G$ for some finite group $G$ of automorphisms of $E$.

# Core Definition

**Theorem 23.19.** Let $E$ be a field extension of $F$. Then the following statements are equivalent (Judson, p. 313):

1. $E$ is a finite, normal, separable extension of $F$.
2. $E$ is a splitting field over $F$ of a separable polynomial.
3. $F = E_G$ for some finite group $G$ of automorphisms of $E$.

An extension satisfying these conditions is called a **Galois extension**.

# Prerequisites

- **Normal extension** — One of the conditions for a Galois extension
- **Separable extension** — The other condition
- **Extension field** — Galois extensions are field extensions

# Key Properties

1. For Galois extensions: $|G(E/F)| = [E:F]$
2. The Fundamental Theorem of Galois Theory applies to Galois extensions
3. In characteristic 0, every finite normal extension is Galois (separability is automatic)
4. Every finite extension of a finite field is Galois

# Context & Application

Galois extensions are the extensions where the full power of Galois theory applies. The Fundamental Theorem establishes a perfect correspondence between subgroups and intermediate fields only for Galois extensions.

# Examples

**Example 1**: $\mathbb{Q}(\sqrt{3}, \sqrt{5})/\mathbb{Q}$ is Galois (splitting field of $(x^2-3)(x^2-5)$).

**Example 2**: $\mathbb{Q}(\sqrt[3]{2})/\mathbb{Q}$ is not Galois (not normal: $x^3 - 2$ does not split in $\mathbb{Q}(\sqrt[3]{2})$).

# Relationships

## Builds Upon
- **Normal extension** — Required condition
- **Separable extension** — Required condition

## Enables
- **Fundamental Theorem of Galois Theory** — Applies to Galois extensions

## Related
- **Galois group** — The group $G(E/F)$ in a Galois extension

# Common Confusions

- **Confusion**: Thinking every field extension is Galois
  **Clarification**: The extension must be normal and separable; $\mathbb{Q}(\sqrt[3]{2})/\mathbb{Q}$ is not Galois

# Source Reference

Chapter 23: Galois Theory, Section 23.2, pages 313–314. Theorem 23.19.

# Verification Notes

- Definition source: Synthesized from Theorem 23.19, p. 313
- Confidence: HIGH — explicit equivalence theorem
- Cross-reference status: Verified
- Uncertainties: None
