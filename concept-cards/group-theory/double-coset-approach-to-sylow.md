---
# === CORE IDENTIFICATION ===
concept: Double Coset Approach to Sylow Theorems
slug: double-coset-approach-to-sylow

# === CLASSIFICATION ===
category: sylow-theory
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "Group Theory"
source_slug: group-theory
authors: "J.S. Milne"
chapter: "The Sylow Theorems; Applications"
chapter_number: 5
pdf_page: 80
section: "Alternative approach to the Sylow theorems"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - alternative proof of Sylow theorems

# === TYPED RELATIONSHIPS ===
prerequisites:
  - sylow-p-subgroup
  - double-coset
  - sylow-subgroup-of-gln
extends: []
related:
  - sylow-first-theorem
  - sylow-second-theorem
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Is there an alternative proof of the Sylow theorems?"
---

# Quick Definition

The Sylow theorems can be proved using double cosets: if P is a Sylow p-subgroup of G, then for any subgroup H, decomposing G into HaP double cosets shows that some conjugate of P intersects H in a Sylow p-subgroup of H.

# Core Definition

**Theorem 5.12.** Let G be a group and let P be a Sylow p-subgroup of G. For any subgroup H of G, there exists an a in G such that H intersect aPa^{-1} is a Sylow p-subgroup of H.

The proof uses the double coset decomposition |G| = sum_a |HaP| = sum_a |H||P|/|H intersect aPa^{-1}|, from which dividing by |P| gives |G|/|P| = sum_a (H : H intersect aPa^{-1}). Since |G|/|P| is not divisible by p, some summand (H : H intersect aPa^{-1}) is coprime to p.

(Milne, Theorem 5.12, p. 80-81)

# Prerequisites

- **sylow-p-subgroup** -- existence in GL_n(F_p) is assumed
- **double-coset** -- the decomposition G = union HaP
- **sylow-subgroup-of-gln** -- provides the initial Sylow subgroup

# Key Properties

1. This approach derives Sylow I from the existence of Sylow subgroups in GL_n(F_p) via Cayley's theorem
2. Sylow II(a,c) follow: setting H = P' (a p-subgroup), we get aPa^{-1} contains P'
3. The double coset formula |HaP| = |H||P|/|H intersect aPa^{-1}| is the key identity

# Context & Application

This alternative approach is more conceptual than the original proof and generalizes well. It shows that Sylow subgroups of subgroups arise as intersections with conjugates of a Sylow subgroup of the ambient group.

# Relationships

## Builds Upon
- **double-coset** -- the main technical tool
- **sylow-subgroup-of-gln** -- provides the bootstrap

## Enables
- A cleaner proof of Sylow I and II(a,c)

# Source Reference

Chapter 5, Theorem 5.12 and subsequent proofs, pp. 80-81.

# Verification Notes

- Definition source: Direct from Theorem 5.12
- Confidence rationale: HIGH -- explicit theorem with proof
- Uncertainties: None
