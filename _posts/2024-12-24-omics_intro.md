---
layout: post
title: "Single Cell Omics"
categories: biomath
---

Omics data refers to large-scale biological datasets that capture information about various molecular levels within a biological system. The term "omics" is derived from disciplines such as genomics, transcriptomics, proteomics, metabolomics, and others, each focusing on a specific aspect of biological molecules.

    - Genomics: Complete set of DNA, including genes and non-coding regions.
    - Transcriptomics: RNA molecules, including messenger RNA (mRNA), in a cell or organism.
    - Proteomics: Identification and quantification of all proteins in a biological sample.
    - Metabolomics: Analyzes the complete set of small molecules (metabolites) present in a biological system.
    - Epigenomics: Changes in gene expression that are not caused by alterations in the DNA sequence itself but by chemical modifications to the DNA molecule.

There are multiple cell types in a single tissue - in fact, even within a small subsection of the tissues.
<img src="https://www.frontiersin.org/files/Articles/462487/fevo-08-00092-HTML/image_m/fevo-08-00092-g001.jpg" alt="Image Alt Text" style="max-width: 100%; width: 300px;">


Therefore, bulk RNA sequencing cannot differentiate the transcriptional changes between individual cell types. Therefore, single-cell sequencing is used. 
(Transcriptional changes refer to alterations in the process of transcription, which is the synthesis of RNA from a DNA template. In this process, information encoded in DNA is transcribed into RNA molecules. These changes can be influenced by various factors, including external stimuli, environmental conditions, or cellular signals.)

Sequencing happens with 10x barcoded gel beads. A recording of the sequencing is available here: https://youtu.be/vL7ptq2Dcf0?t=134 (even though a different process (drop-seq) is shown in the video, the overarching goal is the same as with 10x)

![Gel Beads example. Taken from 10xgenomics.com](https://kb.10xgenomics.com/hc/article_attachments/360091053751/Screenshot_2021-03-30_131342.png)


For instance, in the case of RNA sequencing, the indivudial cells suspended in gel beads pass through a PCR machine as shown in the video mentioned above. The PCR spits an output with multiple metadata values. Important ones are as follows:

- 10x Barcode: Required to assign  / read cell values
- UMI: Amplified values from PCR to differentiae for PCR duplicates
- ...
- RNA Sequence
- ...

The final output looks similar to this table:

|        | Cell 1 | Cell 2 | Cell 3 | Cell X |
|---------|---------|---------|---------|---------|
| Gene a  | 3       | 5       | 6       | 3       |
| Gene b  | 3       | 5       | 3       | 2       |
| Gene c  | 5       | 6       | 5       | 4       |
| Gene d  | 5       | 6       | 7       | 8       |
| ...     | ...     | ...     | ...     | ...     |
| Gene z  | 7       | 8       | 4       | 3       |



