---
# === CORE IDENTIFICATION ===
concept: First Isomorphism Theorem
slug: first-isomorphism-theorem

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
aliases:
  - "fundamental theorem on homomorphisms"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - homomorphism
  - kernel
  - quotient-group
  - normal-subgroup
extends: []
related:
  - second-isomorphism-theorem
  - third-isomorphism-theorem
  - image-of-homomorphism
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the First Isomorphism Theorem?"
  - "How are quotient groups related to homomorphisms?"
---

# Quick Definition

The kernel $K$ of a homomorphism $\varphi: G \to G'$ is a normal subgroup of $G$, and the quotient group $G/K$ is isomorphic to the image of $\varphi$. The isomorphism sends $xK \mapsto \varphi(x)$.

# Core Definition

**(16.1) First Isomorphism Theorem.** The kernel $K$ of a homomorphism $\varphi: G \to G'$ is a normal subgroup of $G$, and the correspondence $xK \to \varphi(x)$ is an isomorphism from the quotient group $G/K$ to the image of $\varphi$ (Armstrong, Ch. 16, p. 94).

**Proof outline.** $K$ is a subgroup (closed under products and inverses) and normal ($gxg^{-1} \in K$ for $x \in K$). The map $\psi: G/K \to G'$ defined by $\psi(xK) = \varphi(x)$ is well-defined (if $xK = yK$ then $\varphi(x) = \varphi(y)$), injective (if $\varphi(x) = \varphi(y)$ then $xK = yK$), a homomorphism, and has the same image as $\varphi$.

# Prerequisites

- **Homomorphism** — The theorem concerns a homomorphism $\varphi$
- **Kernel** — The kernel $K$ plays a central role
- **Quotient group** — $G/K$ is the quotient by the kernel
- **Normal subgroup** — The kernel is proved to be normal

# Key Properties

1. $K = \ker(\varphi)$ is normal in $G$
2. The map $\psi(xK) = \varphi(x)$ is well-defined and injective
3. $G/K \cong \operatorname{im}(\varphi)$
4. **Corollary (16.2):** If $\varphi$ is surjective, $G/K \cong G'$
5. **Corollary (16.3):** $\varphi$ is an isomorphism iff it is surjective and $K = \{e\}$

# Construction / Recognition

## To Apply:
1. Identify the homomorphism $\varphi: G \to G'$
2. Compute the kernel $K$
3. Compute the image $\operatorname{im}(\varphi)$
4. Conclude $G/K \cong \operatorname{im}(\varphi)$

# Context & Application

The First Isomorphism Theorem is the fundamental result connecting homomorphisms, normal subgroups, and quotient groups. Armstrong demonstrates its power through seven worked examples, showing how it identifies quotient groups in diverse settings.

# Examples

**Example 1** (p. 94): $\mathbb{Z} \to \mathbb{Z}_n$, $x \mapsto x \pmod{n}$. Kernel $n\mathbb{Z}$, so $\mathbb{Z}/n\mathbb{Z} \cong \mathbb{Z}_n$.

**Example 2** (p. 94): $\mathbb{R} \to C$, $x \mapsto e^{2\pi i x}$. Kernel $\mathbb{Z}$, so $\mathbb{R}/\mathbb{Z} \cong C$ (the circle group).

**Example 3** (p. 94): $O_n \to \{\pm 1\}$, $A \mapsto \det A$. Kernel $SO_n$, so $O_n/SO_n \cong \mathbb{Z}_2$.

**Example 4** (p. 95): $S_4 \to S_3$ via conjugation action on double transpositions. Kernel $V$ (Klein four-group), so $S_4/V \cong S_3$.

**Example 5** (p. 95): $\mathbb{H} - \{0\} \to SO_3$ via quaternion conjugation. Kernel $\mathbb{R} - \{0\}$, so $\mathbb{H} - \{0\}/\mathbb{R} - \{0\} \cong SO_3$.

# Relationships

## Builds Upon
- **Homomorphism** — The theorem applies to homomorphisms
- **Kernel** — Central to the statement
- **Quotient group** — $G/K$ appears in the conclusion

## Enables
- **Second isomorphism theorem** — Generalisation
- **Third isomorphism theorem** — Generalisation

# Common Errors

- **Error**: Forgetting to check that the map $\psi(xK) = \varphi(x)$ is well-defined
  **Correction**: If $xK = yK$ (i.e., $y^{-1}x \in K$), then $\varphi(y^{-1}x) = e$, so $\varphi(x) = \varphi(y)$. This must be verified.

# Common Confusions

- **Confusion**: Thinking the First Isomorphism Theorem says $G \cong G'$
  **Clarification**: It says $G/K \cong \operatorname{im}(\varphi)$. The isomorphism is between the quotient and the image, not between $G$ and $G'$.

# Source Reference

Chapter 16: Homomorphisms, Theorem (16.1), Corollaries (16.2)-(16.3), pp. 94-95 (pdf).

# Verification Notes

- Definition source: Direct from Theorem (16.1)
- Proof: Complete proof given
- Confidence rationale: HIGH — central theorem with full proof
- Uncertainties: None
