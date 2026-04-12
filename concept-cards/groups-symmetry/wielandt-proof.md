---
# === CORE IDENTIFICATION ===
concept: "Wielandt's Proof of the First Sylow Theorem"
slug: wielandt-proof

# === CLASSIFICATION ===
category: finite-group-classification
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "Groups and Symmetry"
source_slug: groups-symmetry
authors: "M.A. Armstrong"
chapter: "The Sylow Theorems"
chapter_number: 20
pdf_page: 120
section: "Proof of (20.1)"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "Wielandt's 1959 proof"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - first-sylow-theorem
  - orbit-stabilizer-theorem
extends: []
related:
  - group-action
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does Wielandt's proof of the First Sylow Theorem work?"
---

# Quick Definition

Wielandt's 1959 proof of the First Sylow Theorem uses a group action on the set of all $p^m$-element subsets of $G$ by left translation. Since the total number of such subsets is not divisible by $p$, some orbit has size not divisible by $p$, and its stabilizer has order $p^m$.

# Core Definition

Armstrong presents Wielandt's proof as follows (p. 120): Let $X$ be the set of all subsets of $G$ with $p^m$ elements. $G$ acts on $X$ by left translation ($g$ sends $A$ to $gA$). The key fact is that $|X| = \binom{kp^m}{p^m}$ is not divisible by $p$ (Exercise 20.14). Therefore some orbit $G(A)$ has size coprime to $p$. By the Orbit-Stabilizer theorem, $|G_A|$ is divisible by $p^m$. But $G_A$ stabilizes $A$, so $|G_A| \le |A| = p^m$. Hence $|G_A| = p^m$.

# Prerequisites

- **First Sylow theorem** -- this is its proof
- **Orbit-Stabilizer theorem** -- the sole tool used

# Key Properties

1. The action is left translation on subsets (not on elements)
2. The binomial coefficient $\binom{kp^m}{p^m}$ is coprime to $p$
3. The stabilizer of a subset $A$ consists of elements $g$ with $gA = A$
4. If $g \in G_A$ and $a \in A$, then $ga \in A$, so $|G_A| \le |A|$

# Context & Application

Armstrong notes this proof makes "repeated use of the Orbit-Stabilizer theorem" and marks each use with an asterisk. The proof is notable for its elegance and for avoiding induction.

# Relationships

## Builds Upon
- **Orbit-Stabilizer theorem** -- the sole ingredient
- **Group action** -- the action on subsets by left translation

## Related
- **First Sylow theorem** -- this is the proof of that theorem

# Source Reference

Chapter 20: The Sylow Theorems, Proof of (20.1), pages 120--121. Attribution to Wielandt (1959) on p. 120.

# Verification Notes

- Proof: Direct from pp. 120--121
- Confidence: HIGH -- complete proof with attribution
