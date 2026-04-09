---
# === CORE IDENTIFICATION ===
concept: Sylow Normalizer Lemma
slug: sylow-normalizer-lemma

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
pdf_page: 78
section: "The Sylow theorems"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - sylow-p-subgroup
  - normalizer
  - p-group
extends: []
related:
  - sylow-second-theorem
  - normalizer-and-sylow
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "When does a p-subgroup normalizing a Sylow p-subgroup imply containment?"
---

# Quick Definition

If P is a Sylow p-subgroup and H is a p-subgroup that normalizes P (i.e., H is contained in N_G(P)), then H is contained in P. In particular, no Sylow p-subgroup other than P normalizes P.

# Core Definition

**Lemma 5.7.** Let P be a Sylow p-subgroup of G, and let H be a p-subgroup. If H normalizes P, i.e., if H is a subset of N_G(P), then H is a subset of P. In particular, no Sylow p-subgroup of G other than P normalizes P.

(Milne, Lemma 5.7, p. 78)

# Prerequisites

- **sylow-p-subgroup** -- P is a Sylow p-subgroup
- **normalizer** -- N_G(P) = {g in G : gPg^{-1} = P}
- **p-group** -- H is a p-group

# Key Properties

1. Since H normalizes P, the product HP is a subgroup of N_G(P)
2. HP/P is isomorphic to H/(H intersect P), which is a p-group
3. But |P| is the highest power of p dividing |G|, hence |HP| can only have |P| as its p-part
4. Therefore (HP : P) = 1 and H is a subset of P

# Construction / Recognition

This lemma is used as a tool in the proof of Sylow II. Whenever you need to show that a p-subgroup is contained in a particular Sylow subgroup, check whether it normalizes that Sylow subgroup.

# Context & Application

This is the key technical lemma enabling the proof that all Sylow p-subgroups are conjugate. It is also used to show that the only fixed point of a Sylow p-subgroup P acting by conjugation on the set of all Sylow p-subgroups is P itself.

# Examples

**Example 1** (p. 78-79): In the proof of Sylow II(a), P acts on the set of Sylow p-subgroups by conjugation. A Sylow subgroup Q is a fixed point iff P normalizes Q, which by Lemma 5.7 means P = Q.

# Relationships

## Builds Upon
- **normalizer** -- the hypothesis involves the normalizer

## Enables
- **sylow-second-theorem** -- this lemma is essential to the proof of conjugacy

## Related
- **normalizer-and-sylow** -- relates normalizers to Sylow counting

# Common Errors

- **Error**: Applying the lemma when H is not a p-group
  **Correction**: The conclusion requires H to be a p-group; for a general subgroup normalizing P, there is no containment conclusion

# Source Reference

Chapter 5, Lemma 5.7, p. 78.

# Verification Notes

- Definition source: Direct from Lemma 5.7
- Confidence rationale: HIGH -- explicitly stated lemma with proof
- Uncertainties: None
