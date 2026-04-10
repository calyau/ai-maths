---
# === CORE IDENTIFICATION ===
concept: Fundamental Domain for SL₂
slug: fundamental-domain-sl2

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
pdf_page: 403
section: "A fundamental domain for SL₂"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - standard fundamental domain
  - modular domain

# === TYPED RELATIONSHIPS ===
prerequisites:
  - arithmetic-subgroup
  - upper-half-plane
extends: []
related:
  - reduction-theory
  - equivalence-of-quadratic-forms
  - siegel-set
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do arithmetic subgroups relate to discrete subgroups of Lie groups?"
---

# Quick Definition

The standard fundamental domain for $\mathrm{SL}_2(\mathbb{Z})$ acting on the upper half-plane $\mathcal{H}$ is the set $D = \{z \in \mathbb{C} \mid -1/2 \leq \Re(z) \leq 1/2, |z| \geq 1\}$. Every point of $\mathcal{H}$ is equivalent to a point in $D$, and no two interior points of $D$ are equivalent.

# Core Definition

$\mathrm{SL}_2(\mathbb{R})$ acts on the upper half-plane $\mathcal{H} = \{z \in \mathbb{C} \mid \Im(z) > 0\}$ by $\begin{pmatrix} a & b \\ c & d\end{pmatrix} z = \frac{az+b}{cz+d}$.

"Let $D$ be the subset $\{z \in \mathbb{C} \mid -1/2 \leq \Re(z) \leq 1/2, |z| \geq 1\}$ of $\mathcal{H}$. Then $\mathcal{H} = \mathrm{SL}_2(\mathbb{Z}) \cdot D$, and if two points of $D$ lie in the same orbit then neither is in the interior of $D$." (Proposition 9.1, Milne, p. 403)

# Prerequisites

- **Arithmetic subgroup** — $\mathrm{SL}_2(\mathbb{Z})$ is the prototypical arithmetic subgroup
- **Upper half-plane** — the space on which $\mathrm{SL}_2$ acts

# Key Properties

1. The action of $\mathrm{SL}_2(\mathbb{R})$ on $\mathcal{H}$ is transitive; the stabilizer of $i$ is $\mathrm{SO}(2)$
2. $\mathcal{H} \simeq \mathrm{SL}_2(\mathbb{R})/\mathrm{SO}(2)$ as a smooth manifold
3. $\Im\left(\frac{az+b}{cz+d}\right) = \frac{(ad-bc)\Im(z)}{|cz+d|^2}$
4. $D$ tiles $\mathcal{H}$ under the action of $\mathrm{SL}_2(\mathbb{Z})$
5. The generators $S = \begin{pmatrix} 0 & -1 \\ 1 & 0\end{pmatrix}$ ($z \mapsto -1/z$) and $T = \begin{pmatrix} 1 & 1 \\ 0 & 1\end{pmatrix}$ ($z \mapsto z+1$) suffice to move any point into $D$

# Construction / Recognition

## To Find the Representative of $z_0$ in $D$:
1. Choose $\gamma \in \mathrm{SL}_2(\mathbb{Z})$ maximizing $\Im(\gamma(z_0))$
2. Apply $T^m$ to ensure $-1/2 \leq \Re(T^m\gamma(z_0)) \leq 1/2$
3. If $|T^m\gamma(z_0)| < 1$, applying $S$ would increase the imaginary part, contradicting the choice of $\gamma$
4. Hence $T^m\gamma(z_0) \in D$

# Context & Application

The fundamental domain for $\mathrm{SL}_2(\mathbb{Z})$ is the simplest case of reduction theory. It demonstrates the key ideas (maximizing the imaginary part, using translations and inversions) that generalize to Siegel sets and reduction theory for higher-rank groups.

# Examples

**Example 1** (p. 403): The domain $D$ has vertices at $e^{2\pi i/3}$, $e^{\pi i/3}$, and $i\infty$, with sides identified by $S$ and $T$.

**Example 2** (p. 404-405): The fundamental domain gives finite covolume: $\int_D \frac{dxdy}{y^2} \leq \int_{\sqrt{3}/2}^\infty \int_{-1/2}^{1/2} \frac{dxdy}{y^2} < \infty$, showing $\mathrm{SL}_2(\mathbb{Z})$ has finite covolume in $\mathrm{SL}_2(\mathbb{R})$.

# Relationships

## Builds Upon
- **Arithmetic subgroup** — $\mathrm{SL}_2(\mathbb{Z})$ is the model arithmetic subgroup

## Enables
- **Equivalence of quadratic forms** — reduced forms correspond to points in $D$
- **Reduction theory** — generalizes the fundamental domain to higher-rank groups
- **Siegel set** — the higher-rank analogue of $D$

# Common Errors

- **Error**: Forgetting boundary identifications when counting equivalent points
  **Correction**: Points on the boundary of $D$ may be $\mathrm{SL}_2(\mathbb{Z})$-equivalent; only interior points are inequivalent

# Common Confusions

- **Confusion**: Thinking $D$ is a fundamental domain in the strict sense
  **Clarification**: $D$ is a fundamental domain up to boundary identifications; it is a "fundamental set" rather than a strict fundamental domain

# Source Reference

Chapter VII: Arithmetic Subgroups, Section 9, pages 403-404. Proposition 9.1.

# Verification Notes

- Definition source: Direct from Proposition 9.1
- Confidence: HIGH — explicit statement and proof
- Uncertainties: None
- Cross-reference status: Verified
