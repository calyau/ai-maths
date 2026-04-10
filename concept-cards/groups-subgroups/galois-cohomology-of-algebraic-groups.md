---
# === CORE IDENTIFICATION ===
concept: Galois Cohomology of Algebraic Groups
slug: galois-cohomology-of-algebraic-groups

# === CLASSIFICATION ===
category: galois-cohomology
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "The Structure of Reductive Groups: General Case"
chapter_number: 6
pdf_page: 385
section: "The cohomology of algebraic groups; applications"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "H^i(k, G)"
  - Galois cohomology of G

# === TYPED RELATIONSHIPS ===
prerequisites:
  - algebraic-group
  - noncommutative-galois-cohomology
extends:
  - noncommutative-galois-cohomology
related:
  - form-of-algebraic-group
  - inner-form
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does Galois cohomology classify forms of algebraic groups?"
  - "What must I know before understanding Galois cohomology of algebraic groups?"
---

# Quick Definition

For an algebraic group $G$ over a field $k$, the Galois cohomology $H^i(k, G)$ is defined as $H^i(\mathrm{Gal}(k^{\mathrm{al}}/k), G(k^{\mathrm{al}}))$. It classifies forms of $G$ and measures obstructions in exact sequences of algebraic groups.

# Core Definition

When $G$ is an algebraic group over $k$, the group $G(k^{\mathrm{al}})$ satisfies the continuity condition $G(k^{\mathrm{al}}) = \bigcup G(K)$ where $K$ ranges over finite extensions of $k$ in $k^{\mathrm{al}}$. One writes $H^i(k, G)$ for $H^i(\mathrm{Gal}(k^{\mathrm{al}}/k), G(k^{\mathrm{al}}))$ (Milne, p. 385).

An exact sequence $1 \to G' \to G \to G'' \to 1$ of algebraic groups over $k$ gives rise to an exact sequence:
$$1 \to G'(k) \to G(k) \to G''(k) \to H^1(k, G') \to H^1(k, G) \to H^1(k, G'')$$
(Milne, p. 385).

# Prerequisites

- **Algebraic group** — $G$ must be an algebraic group for $G(k^{\mathrm{al}})$ to be defined
- **Noncommutative Galois cohomology** — provides the framework for $H^0$ and $H^1$

# Key Properties

1. $H^0(k, G) = G(k)$, the $k$-rational points
2. $H^1(k, \mathrm{GL}_n) = 1$ (Hilbert's Theorem 90 generalized)
3. $H^1(k, \mathrm{SL}_n) = 1$ and $H^1(k, \mathrm{Sp}_n) = 1$
4. If $k$ is finite and $G$ is connected, then $H^1(k, G) = 1$ (Lang's theorem, 1.23)
5. If $k$ is $p$-adic and $G$ is simply connected semisimple, then $H^1(k, G) = 1$ (Kneser's theorem, 1.24)
6. For $G$ simply connected over $\mathbb{Q}$: $H^1(\mathbb{Q}, G) \simeq H^1(\mathbb{R}, G)$ (Hasse principle, 1.25a)

# Construction / Recognition

## To Compute $H^1(k, G)$:
1. Use vanishing theorems if applicable ($\mathrm{GL}_n$, $\mathrm{SL}_n$, $\mathrm{Sp}$, finite fields, $p$-adic for simply connected)
2. Use exact sequences to reduce to known cases
3. For orthogonal groups, classify quadratic forms over $k$
4. For simply connected groups over $\mathbb{Q}$, reduce to $H^1(\mathbb{R}, G)$

# Context & Application

Galois cohomology of algebraic groups is the main tool for studying algebraic groups over non-algebraically closed fields. The vanishing and computation results (1.23-1.25) are deep theorems connecting the theory to number theory. The Hasse principle (1.25b) for adjoint groups and orthogonal groups connects local and global information.

# Examples

**Example 1** (p. 390): $H^1(k, \mathrm{O}(\phi))$ classifies isomorphism classes of quadratic spaces of the same dimension as $(V, \phi)$. Over $k^{\mathrm{al}}$, all quadratic spaces of the same dimension are isomorphic.

**Example 2** (p. 393): For a simply connected group $G$ over $\mathbb{Q}$, $H^1(\mathbb{Q}, G) \simeq H^1(\mathbb{R}, G)$, so classification reduces to the real case.

**Example 3** (p. 393): The Hasse principle for quadratic forms: two quadratic spaces over $\mathbb{Q}$ are isomorphic if and only if they become isomorphic over $\mathbb{Q}_p$ for all $p$ (including $p = \infty$).

# Relationships

## Builds Upon
- **Noncommutative Galois cohomology** — specialized to the absolute Galois group

## Enables
- **Form of algebraic group** — classified by $H^1(k, \mathrm{Aut}(G))$
- **Inner form** — inner forms correspond to $H^1(k, G^{\mathrm{ad}})$
- **Tits index** — the classification of non-split groups uses cohomological data

## Related
- **Anisotropic kernel** — the anisotropic part relates to the cohomological classification

# Common Errors

- **Error**: Applying the Hasse principle to all algebraic groups
  **Correction**: The Hasse principle $H^1(\mathbb{Q}, G) \hookrightarrow \prod H^1(\mathbb{Q}_p, G)$ holds for adjoint and orthogonal groups (1.25b), but not in general

# Common Confusions

- **Confusion**: Thinking $H^1(k, G) = 1$ for all semisimple groups
  **Clarification**: $H^1 = 1$ for simply connected groups over $p$-adic fields, but not for all semisimple groups or all fields. The orthogonal group provides counterexamples.

# Source Reference

Chapter VI: The Structure of Reductive Groups: General Case, Sections 1a-1e, pages 384-394.

# Verification Notes

- Definition source: Direct from p. 385
- Key results 1.23-1.25 are stated on p. 393
- Confidence: HIGH — explicit definitions and theorem statements
- Uncertainties: None
- Cross-reference status: Verified
