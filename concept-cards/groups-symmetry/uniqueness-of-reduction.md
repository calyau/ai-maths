---
# === CORE IDENTIFICATION ===
concept: Uniqueness of Reduction
slug: uniqueness-of-reduction

# === CLASSIFICATION ===
category: combinatorial-group-theory
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "Groups and Symmetry"
source_slug: groups-symmetry
authors: "M.A. Armstrong"
chapter: "Free Groups and Presentations"
chapter_number: 27
pdf_page: 173
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "Theorem 27.1"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - word
  - reduced-word
extends: []
related:
  - free-group
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Why does every word reduce to a unique reduced word?"
---

# Quick Definition

Each word in an alphabet X can be simplified to only one reduced word, regardless of the order in which the reduction steps are carried out. This is Theorem 27.1, which ensures the free group is well-defined.

# Core Definition

"(27.1) Theorem. Each word can be simplified to only one reduced word" (Armstrong, Ch. 27, p. 174). The proof uses a permutation argument: for each generator x, define a permutation phi_x of the set of reduced words by phi_x(w) = xw-bar (the reduction of xw). If a word u reduces to both v and w, then the associated permutations satisfy phi_v = phi_u = phi_w, and applying these to the empty word gives v = w.

# Prerequisites

- **Word** -- The objects being reduced
- **Reduced word** -- The canonical form

# Key Properties

1. The reduction process is confluent: all reduction orders yield the same result
2. The proof uses Cayley-type permutation representation
3. Each generator x defines a permutation phi_x on the set of reduced words
4. The key insight: if u reduces to v in any way, then phi_u = phi_v as permutations
5. Applying phi_v and phi_w to the empty word forces v = w

# Construction / Recognition

## Proof Idea (Armstrong, p. 174)
1. For each x in X, define phi_x: reduced words -> reduced words by phi_x(w) = xw-bar
2. For a word u = x_1^{m_1}...x_s^{m_s}, define phi_u = (phi_{x_1})^{m_1}...(phi_{x_s})^{m_s}
3. Permutations form a group, so if u reduces to w in any way, phi_u = phi_w
4. If u reduces to both v and w: phi_v = phi_u = phi_w
5. But phi_v(empty) = v and phi_w(empty) = w, so v = w

# Context & Application

This theorem is the foundational result that makes free groups well-defined. Without it, the "multiplication" in F(X) (concatenate and reduce) might depend on how the reduction is carried out, and the group structure would break down. Armstrong notes the proof is "reminiscent of the proof of Cayley's theorem."

# Examples

**Example 1** (p. 174): The word w = x^{-3}x^2y^5y^{-5}x^7z^2z^{-2}x^{-1}xzy^2x^{-1} is reduced in two different ways, both yielding x^6zy^2x^{-1}.

# Relationships

## Enables
- **Free group** -- The free group construction depends on uniqueness of reduction

## Related
- **Word** -- The objects being reduced
- **Reduced word** -- The unique outcome

# Common Errors

- **Error**: Attempting to prove uniqueness by showing reduction is deterministic
  **Correction**: Reduction is NOT deterministic (there may be many valid next steps); the theorem shows all paths lead to the same endpoint

# Common Confusions

- **Confusion**: Thinking the theorem is obvious
  **Clarification**: It is not obvious that different reduction orders yield the same result; the proof requires a non-trivial argument involving permutations

# Source Reference

Chapter 27: Free Groups and Presentations, Theorem 27.1 and proof, page 174 (pdf p. 174).

# Verification Notes

- Theorem: Directly quoted from Armstrong p. 174
- Proof: Complete in source using permutation argument
- Confidence: HIGH -- named theorem with complete proof
- Cross-references: Verified against planned extractions
- Uncertainties: None
