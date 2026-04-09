---
# === CORE IDENTIFICATION ===
concept: p-Group Fixed Point Lemma
slug: p-group-fixed-point-lemma

# === CLASSIFICATION ===
category: sylow-theory
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Group Theory"
source_slug: group-theory
authors: "J.S. Milne"
chapter: "The Sylow Theorems; Applications"
chapter_number: 5
pdf_page: 77
section: "The Sylow theorems"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - fixed point lemma for p-groups

# === TYPED RELATIONSHIPS ===
prerequisites:
  - p-group
  - group-action
extends: []
related:
  - sylow-first-theorem
  - sylow-second-theorem
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does a p-group action constrain the size of the fixed point set?"
  - "What must I know before understanding the Sylow theorems?"
---

# Quick Definition

When a p-group H acts on a finite set X, the number of fixed points is congruent to |X| modulo p. This is the key counting tool behind the Sylow theorems.

# Core Definition

**Lemma 5.1.** Let H be a p-group acting on a finite set X, and let X^H be the set of points fixed by H. Then

|X| is congruent to |X^H| (mod p).

(Milne, Lemma 5.1, p. 77)

# Prerequisites

- **p-group** -- the acting group must have order a power of p
- **group-action** -- orbits and stabilizers; the orbit-stabilizer relation (G : Stab(x)) = |orbit of x|

# Key Properties

1. Each orbit has size dividing |H|, hence is a power of p
2. An orbit has size 1 if and only if the point is fixed
3. Non-singleton orbits have sizes divisible by p
4. Summing over orbits: |X| = |X^H| + (terms divisible by p)

# Construction / Recognition

## To Apply:
1. Identify a p-group H acting on a finite set X
2. Compute |X| modulo p
3. Conclude |X^H| has the same residue mod p
4. In particular, if p does not divide |X|, then X^H is nonempty

# Context & Application

This lemma is the engine behind the Sylow theorems. Applied to a p-group acting on itself by conjugation, it gives p | |Z(H)|. Applied to a Sylow p-subgroup acting on the set of all Sylow p-subgroups by conjugation, it yields the congruence s_p congruent to 1 mod p.

# Examples

**Example 1** (p. 77): When a p-group H acts on itself by conjugation, X = H and X^H = Z(H), giving |Z(H)| congruent to |H| mod p, hence p divides |Z(H)|.

**Example 2** (p. 78-79): In the proof of Sylow II, P acts on the set X of Sylow p-subgroups by conjugation. Since |X| = s_p is not divisible by p, X^P is nonempty, yielding containment of p-subgroups in Sylow subgroups.

# Relationships

## Builds Upon
- **group-action** -- orbit-stabilizer relation

## Enables
- **sylow-first-theorem** -- proof uses the lemma indirectly via orbit counting
- **sylow-second-theorem** -- proof directly applies this lemma

## Related
- **class-equation** -- a more detailed version of the same counting principle

# Common Errors

- **Error**: Applying the lemma to non-p-groups
  **Correction**: The result requires H to be a p-group; for a general group, orbit sizes need not be powers of p

# Common Confusions

- **Confusion**: Thinking the lemma says something about fixed points of individual elements
  **Clarification**: X^H is the set of points fixed by *every* element of H, not by some element

# Source Reference

Chapter 5, Lemma 5.1, p. 77.

# Verification Notes

- Definition source: Direct from Lemma 5.1, p. 77
- Confidence rationale: HIGH -- explicitly stated and proved lemma
- Uncertainties: None
