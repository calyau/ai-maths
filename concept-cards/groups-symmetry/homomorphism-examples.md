---
# === CORE IDENTIFICATION ===
concept: Homomorphism Examples
slug: homomorphism-examples

# === CLASSIFICATION ===
category: homomorphisms
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Groups and Symmetry"
source_slug: groups-symmetry
authors: "M.A. Armstrong"
chapter: "Homomorphisms"
chapter_number: 16
pdf_page: 93
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - homomorphism
  - first-isomorphism-theorem
  - kernel
extends: []
related:
  - quotient-group
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What are standard examples of homomorphisms?"
  - "How does the First Isomorphism Theorem work in practice?"
---

# Quick Definition

Armstrong presents eight important surjective homomorphisms with their kernels, demonstrating the First Isomorphism Theorem across number theory, linear algebra, topology, and group theory.

# Core Definition

Armstrong lists examples (i)-(viii) of surjective homomorphisms, each illustrating the First Isomorphism Theorem: the quotient by the kernel is isomorphic to the image (Armstrong, Ch. 16, pp. 94-95).

# Prerequisites

- **Homomorphism** — Each example is verified as a homomorphism
- **First isomorphism theorem** — Applied to identify quotient groups
- **Kernel** — Computed for each example

# Key Properties

The eight examples and their kernels:

1. $\mathbb{Z} \to \mathbb{Z}_n$, $x \mapsto x \pmod{n}$. $K = n\mathbb{Z}$, $\mathbb{Z}/n\mathbb{Z} \cong \mathbb{Z}_n$.
2. $\mathbb{R} \to C$, $x \mapsto e^{2\pi i x}$. $K = \mathbb{Z}$, $\mathbb{R}/\mathbb{Z} \cong C$.
3. $\mathbb{C} - \{0\} \to C$, $z \mapsto z/|z|$. $K = \mathbb{R}^{\text{pos}}$, $(\mathbb{C} - \{0\})/\mathbb{R}^{\text{pos}} \cong C$.
4. $O_n \to \{\pm 1\}$, $A \mapsto \det A$. $K = SO_n$, $O_n/SO_n \cong \mathbb{Z}_2$.
5. $U_n \to C$, $A \mapsto \det A$. $K = SU_n$, $U_n/SU_n \cong C$.
6. $C \to C$, $z \mapsto z^2$. $K = \{\pm 1\}$, $C/\{\pm 1\} \cong C$.
7. $S_4 \to S_3$ via conjugation on double transpositions. $K = V$, $S_4/V \cong S_3$.
8. $\mathbb{H} - \{0\} \to SO_3$ via quaternion conjugation. $K = \mathbb{R} - \{0\}$, $(\mathbb{H} - \{0\})/(\mathbb{R} - \{0\}) \cong SO_3$.

# Construction / Recognition

## Pattern for Each Example:
1. Define $\varphi: G \to G'$
2. Verify $\varphi(xy) = \varphi(x)\varphi(y)$
3. Verify surjectivity
4. Compute the kernel $K$
5. Conclude $G/K \cong G'$ by Corollary (16.2)

# Context & Application

These examples demonstrate the breadth of the First Isomorphism Theorem. They connect diverse areas: number theory (modular arithmetic), complex analysis (circle group), linear algebra (determinant), and quaternion geometry.

Example (vii) is particularly notable: it constructs a surjective homomorphism $S_4 \to S_3$ by observing that conjugation in $S_4$ permutes the three double transpositions $(12)(34)$, $(13)(24)$, $(14)(23)$.

Example (viii) connects quaternions to rotations: conjugation by a non-zero quaternion induces a rotation of $\mathbb{R}^3$, giving a homomorphism $\mathbb{H} - \{0\} \to SO_3$.

# Examples

All eight examples are listed above in Key Properties.

# Relationships

## Builds Upon
- **First isomorphism theorem** — Applied in each example
- **Kernel** — Computed for each example

## Related
- **Quotient group** — Each example identifies a quotient group

# Common Errors

- **Error**: Assuming all the examples are obvious without verification
  **Correction**: Each requires checking that $\varphi$ is indeed a homomorphism and identifying the kernel. Example (vii) in particular requires a non-trivial construction.

# Common Confusions

- **Confusion**: Thinking these examples all follow the same pattern
  **Clarification**: While the theorem is uniform, the homomorphisms come from diverse constructions: modular reduction, exponential map, determinant, norm, squaring, conjugation action, quaternion conjugation.

# Source Reference

Chapter 16: Homomorphisms, Examples (i)-(viii), pp. 94-95 (pdf).

# Verification Notes

- Definition source: Direct from pp. 94-95
- Confidence rationale: HIGH — all examples explicitly listed
- Uncertainties: Some verification details left to the reader
