---
# === CORE IDENTIFICATION ===
concept: Error-Detecting Code
slug: error-detecting-code

# === CLASSIFICATION ===
category: applications-coding
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Algebraic Coding Theory"
chapter_number: 8
pdf_page: 104
section: "8.1 Error-Detecting and Correcting Codes"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - error-correcting-code
  - parity-check-bit
  - minimum-distance
contrasts_with:
  - error-correcting-code

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an error-detecting code?"
  - "How does error detection work?"
---

# Quick Definition

An error-detecting code can determine that an error has occurred during transmission but cannot identify or correct the specific error. Detection requires minimum distance $d_{\min} \geq 2$.

# Core Definition

An error-detecting code is a coding scheme that can recognize when a received word is not a valid codeword, indicating that a transmission error has occurred. "Adding a parity check bit allows the detection of all single errors" (Judson, p. 106). A code with minimum distance $d_{\min} = 2n + 1$ can detect up to $2n$ errors (Theorem 8.13).

# Prerequisites

This is an introductory concept in coding theory.

# Key Properties

1. Requires $d_{\min} \geq 2$ for single error detection
2. A code with $d_{\min} = 2n + 1$ can detect up to $2n$ errors
3. Detection means recognizing that the received word is not a codeword
4. Cannot correct errors; can only request retransmission
5. Even parity is the simplest error-detecting scheme

# Construction / Recognition

## To Detect Errors:
1. Receive a word
2. Check if it is a valid codeword
3. If not, an error has occurred

# Context & Application

Error detection is essential in communications, computing, and data storage. The simplest example is even parity, used in ASCII and computer memory.

# Examples

**Example 1** (p. 105-106): ASCII even parity: the leftmost bit is set so the total number of 1s is even. If a received 8-tuple has an odd number of 1s, an error is detected.

# Relationships

## Enables
- **Parity Check Bit** — Simplest error detection mechanism

## Related
- **Minimum Distance** — Determines detection capability

## Contrasts With
- **Error-Correcting Code** — Can also fix errors, not just detect them

# Common Errors

- **Error**: Assuming detection means correction
  **Correction**: Error detection only identifies that an error occurred; it cannot determine which bit is wrong

# Common Confusions

- **Confusion**: Thinking even parity detects multiple errors
  **Clarification**: Even parity detects only odd numbers of errors; an even number of errors goes undetected

# Source Reference

Chapter 8: Algebraic Coding Theory, Section 8.1, pages 104-111.

# Verification Notes

- Definition source: Synthesized from pp. 104-111
- Confidence rationale: Concept thoroughly discussed with examples
- Uncertainties: None
- Cross-reference status: Verified
