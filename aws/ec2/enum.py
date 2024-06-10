from enum import Enum


class EC2InstanceType(Enum):
    A1_MEDIUM = "a1.medium"
    A1_LARGE = "a1.large"
    A1_XLARGE = "a1.xlarge"
    A1_2XLARGE = "a1.2xlarge"
    A1_4XLARGE = "a1.4xlarge"
    A1_METAL = "a1.metal"
    C1_MEDIUM = "c1.medium"
    C1_XLARGE = "c1.xlarge"
    C3_LARGE = "c3.large"
    C3_XLARGE = "c3.xlarge"
    C3_2XLARGE = "c3.2xlarge"
    C3_4XLARGE = "c3.4xlarge"
    C3_8XLARGE = "c3.8xlarge"
    C4_LARGE = "c4.large"
    C4_XLARGE = "c4.xlarge"
    C4_2XLARGE = "c4.2xlarge"
    C4_4XLARGE = "c4.4xlarge"
    C4_8XLARGE = "c4.8xlarge"
    C5_LARGE = "c5.large"
    C5_XLARGE = "c5.xlarge"
    C5_2XLARGE = "c5.2xlarge"
    C5_4XLARGE = "c5.4xlarge"
    C5_9XLARGE = "c5.9xlarge"
    C5_12XLARGE = "c5.12xlarge"
    C5_18XLARGE = "c5.18xlarge"
    C5_24XLARGE = "c5.24xlarge"
    C5_METAL = "c5.metal"
    C5A_LARGE = "c5a.large"
    C5A_XLARGE = "c5a.xlarge"
    C5A_2XLARGE = "c5a.2xlarge"
    C5A_4XLARGE = "c5a.4xlarge"
    C5A_8XLARGE = "c5a.8xlarge"
    C5A_12XLARGE = "c5a.12xlarge"
    C5A_16XLARGE = "c5a.16xlarge"
    C5A_24XLARGE = "c5a.24xlarge"
    C5AD_LARGE = "c5ad.large"
    C5AD_XLARGE = "c5ad.xlarge"
    C5AD_2XLARGE = "c5ad.2xlarge"
    C5AD_4XLARGE = "c5ad.4xlarge"
    C5AD_8XLARGE = "c5ad.8xlarge"
    C5AD_12XLARGE = "c5ad.12xlarge"
    C5AD_16XLARGE = "c5ad.16xlarge"
    C5AD_24XLARGE = "c5ad.24xlarge"
    C5D_LARGE = "c5d.large"
    C5D_XLARGE = "c5d.xlarge"
    C5D_2XLARGE = "c5d.2xlarge"
    C5D_4XLARGE = "c5d.4xlarge"
    C5D_9XLARGE = "c5d.9xlarge"
    C5D_12XLARGE = "c5d.12xlarge"
    C5D_18XLARGE = "c5d.18xlarge"
    C5D_24XLARGE = "c5d.24xlarge"
    C5D_METAL = "c5d.metal"
    C5N_LARGE = "c5n.large"
    C5N_XLARGE = "c5n.xlarge"
    C5N_2XLARGE = "c5n.2xlarge"
    C5N_4XLARGE = "c5n.4xlarge"
    C5N_9XLARGE = "c5n.9xlarge"
    C5N_18XLARGE = "c5n.18xlarge"
    C5N_METAL = "c5n.metal"
    C6G_MEDIUM = "c6g.medium"
    C6G_LARGE = "c6g.large"
    C6G_XLARGE = "c6g.xlarge"
    C6G_2XLARGE = "c6g.2xlarge"
    C6G_4XLARGE = "c6g.4xlarge"
    C6G_8XLARGE = "c6g.8xlarge"
    C6G_12XLARGE = "c6g.12xlarge"
    C6G_16XLARGE = "c6g.16xlarge"
    C6G_METAL = "c6g.metal"
    C6GD_MEDIUM = "c6gd.medium"
    C6GD_LARGE = "c6gd.large"
    C6GD_XLARGE = "c6gd.xlarge"
    C6GD_2XLARGE = "c6gd.2xlarge"
    C6GD_4XLARGE = "c6gd.4xlarge"
    C6GD_8XLARGE = "c6gd.8xlarge"
    C6GD_12XLARGE = "c6gd.12xlarge"
    C6GD_16XLARGE = "c6gd.16xlarge"
    C6GD_METAL = "c6gd.metal"
    C6GN_MEDIUM = "c6gn.medium"
    C6GN_LARGE = "c6gn.large"
    C6GN_XLARGE = "c6gn.xlarge"
    C6GN_2XLARGE = "c6gn.2xlarge"
    C6GN_4XLARGE = "c6gn.4xlarge"
    C6GN_8XLARGE = "c6gn.8xlarge"
    C6GN_12XLARGE = "c6gn.12xlarge"
    C6GN_16XLARGE = "c6gn.16xlarge"
    C6I_LARGE = "c6i.large"
    C6I_XLARGE = "c6i.xlarge"
    C6I_2XLARGE = "c6i.2xlarge"
    C6I_4XLARGE = "c6i.4xlarge"
    C6I_8XLARGE = "c6i.8xlarge"
    C6I_12XLARGE = "c6i.12xlarge"
    C6I_16XLARGE = "c6i.16xlarge"
    C6I_24XLARGE = "c6i.24xlarge"
    C6I_32XLARGE = "c6i.32xlarge"
    C6I_METAL = "c6i.metal"
    CC1_4XLARGE = "cc1.4xlarge"
    CC2_8XLARGE = "cc2.8xlarge"
    CG1_4XLARGE = "cg1.4xlarge"
    CR1_8XLARGE = "cr1.8xlarge"
    D2_XLARGE = "d2.xlarge"
    D2_2XLARGE = "d2.2xlarge"
    D2_4XLARGE = "d2.4xlarge"
    D2_8XLARGE = "d2.8xlarge"
    D3_XLARGE = "d3.xlarge"
    D3_2XLARGE = "d3.2xlarge"
    D3_4XLARGE = "d3.4xlarge"
    D3_8XLARGE = "d3.8xlarge"
    D3EN_XLARGE = "d3en.xlarge"
    D3EN_2XLARGE = "d3en.2xlarge"
    D3EN_4XLARGE = "d3en.4xlarge"
    D3EN_6XLARGE = "d3en.6xlarge"
    D3EN_8XLARGE = "d3en.8xlarge"
    D3EN_12XLARGE = "d3en.12xlarge"
    DL1_24XLARGE = "dl1.24xlarge"
    F1_2XLARGE = "f1.2xlarge"
    F1_4XLARGE = "f1.4xlarge"
    F1_16XLARGE = "f1.16xlarge"
    G2_2XLARGE = "g2.2xlarge"
    G2_8XLARGE = "g2.8xlarge"
    G3_4XLARGE = "g3.4xlarge"
    G3_8XLARGE = "g3.8xlarge"
    G3_16XLARGE = "g3.16xlarge"
    G3S_XLARGE = "g3s.xlarge"
    G4AD_XLARGE = "g4ad.xlarge"
    G4AD_2XLARGE = "g4ad.2xlarge"
    G4AD_4XLARGE = "g4ad.4xlarge"
    G4AD_8XLARGE = "g4ad.8xlarge"
    G4AD_16XLARGE = "g4ad.16xlarge"
    G4DN_XLARGE = "g4dn.xlarge"
    G4DN_2XLARGE = "g4dn.2xlarge"
    G4DN_4XLARGE = "g4dn.4xlarge"
    G4DN_8XLARGE = "g4dn.8xlarge"
    G4DN_12XLARGE = "g4dn.12xlarge"
    G4DN_16XLARGE = "g4dn.16xlarge"
    G4DN_METAL = "g4dn.metal"
    G5_XLARGE = "g5.xlarge"
    G5_2XLARGE = "g5.2xlarge"
    G5_4XLARGE = "g5.4xlarge"
    G5_8XLARGE = "g5.8xlarge"
    G5_12XLARGE = "g5.12xlarge"
    G5_16XLARGE = "g5.16xlarge"
    G5_24XLARGE = "g5.24xlarge"
    G5_48XLARGE = "g5.48xlarge"
    G5G_XLARGE = "g5g.xlarge"
    G5G_2XLARGE = "g5g.2xlarge"
    G5G_4XLARGE = "g5g.4xlarge"
    G5G_8XLARGE = "g5g.8xlarge"
    G5G_16XLARGE = "g5g.16xlarge"
    G5G_METAL = "g5g.metal"
    H1_2XLARGE = "h1.2xlarge"
    H1_4XLARGE = "h1.4xlarge"
    H1_8XLARGE = "h1.8xlarge"
    H1_16XLARGE = "h1.16xlarge"
    HS1_8XLARGE = "hs1.8xlarge"
    I2_XLARGE = "i2.xlarge"
    I2_2XLARGE = "i2.2xlarge"
    I2_4XLARGE = "i2.4xlarge"
    I2_8XLARGE = "i2.8xlarge"
    I3_LARGE = "i3.large"
    I3_XLARGE = "i3.xlarge"
    I3_2XLARGE = "i3.2xlarge"
    I3_4XLARGE = "i3.4xlarge"
    I3_8XLARGE = "i3.8xlarge"
    I3_16XLARGE = "i3.16xlarge"
    I3_METAL = "i3.metal"
    I3EN_LARGE = "i3en.large"
    I3EN_XLARGE = "i3en.xlarge"
    I3EN_2XLARGE = "i3en.2xlarge"
    I3EN_3XLARGE = "i3en.3xlarge"
    I3EN_6XLARGE = "i3en.6xlarge"
    I3EN_12XLARGE = "i3en.12xlarge"
    I3EN_24XLARGE = "i3en.24xlarge"
    I3EN_METAL = "i3en.metal"
    IM4GN_LARGE = "im4gn.large"
    IM4GN_XLARGE = "im4gn.xlarge"
    IM4GN_2XLARGE = "im4gn.2xlarge"
    IM4GN_4XLARGE = "im4gn.4xlarge"
    IM4GN_8XLARGE = "im4gn.8xlarge"
    IM4GN_16XLARGE = "im4gn.16xlarge"
    INF1_XLARGE = "inf1.xlarge"
    INF1_2XLARGE = "inf1.2xlarge"
    INF1_6XLARGE = "inf1.6xlarge"
    INF1_24XLARGE = "inf1.24xlarge"
    IS4GEN_LARGE = "is4gen.large"
    IS4GEN_XLARGE = "is4gen.xlarge"
    IS4GEN_2XLARGE = "is4gen.2xlarge"
    IS4GEN_4XLARGE = "is4gen.4xlarge"
    IS4GEN_8XLARGE = "is4gen.8xlarge"
    IS4GEN_16XLARGE = "is4gen.16xlarge"
    M1_SMALL = "m1.small"
    M1_MEDIUM = "m1.medium"
    M1_LARGE = "m1.large"
    M1_XLARGE = "m1.xlarge"
    M2_XLARGE = "m2.xlarge"
    M2_2XLARGE = "m2.2xlarge"
    M2_4XLARGE = "m2.4xlarge"
    M3_MEDIUM = "m3.medium"
    M3_LARGE = "m3.large"
    M3_XLARGE = "m3.xlarge"
    M3_2XLARGE = "m3.2xlarge"
    M4_LARGE = "m4.large"
    M4_XLARGE = "m4.xlarge"
    M4_2XLARGE = "m4.2xlarge"
    M4_4XLARGE = "m4.4xlarge"
    M4_10XLARGE = "m4.10xlarge"
    M4_16XLARGE = "m4.16xlarge"
    M5_LARGE = "m5.large"
    M5_XLARGE = "m5.xlarge"
    M5_2XLARGE = "m5.2xlarge"
    M5_4XLARGE = "m5.4xlarge"
    M5_8XLARGE = "m5.8xlarge"
    M5_12XLARGE = "m5.12xlarge"
    M5_16XLARGE = "m5.16xlarge"
    M5_24XLARGE = "m5.24xlarge"
    M5_METAL = "m5.metal"
    M5A_LARGE = "m5a.large"
    M5A_XLARGE = "m5a.xlarge"
    M5A_2XLARGE = "m5a.2xlarge"
    M5A_4XLARGE = "m5a.4xlarge"
    M5A_8XLARGE = "m5a.8xlarge"
    M5A_12XLARGE = "m5a.12xlarge"
    M5A_16XLARGE = "m5a.16xlarge"
    M5A_24XLARGE = "m5a.24xlarge"
    M5AD_LARGE = "m5ad.large"
    M5AD_XLARGE = "m5ad.xlarge"
    M5AD_2XLARGE = "m5ad.2xlarge"
    M5AD_4XLARGE = "m5ad.4xlarge"
    M5AD_8XLARGE = "m5ad.8xlarge"
    M5AD_12XLARGE = "m5ad.12xlarge"
    M5AD_16XLARGE = "m5ad.16xlarge"
    M5AD_24XLARGE = "m5ad.24xlarge"
    M5D_LARGE = "m5d.large"
    M5D_XLARGE = "m5d.xlarge"
    M5D_2XLARGE = "m5d.2xlarge"
    M5D_4XLARGE = "m5d.4xlarge"
    M5D_8XLARGE = "m5d.8xlarge"
    M5D_12XLARGE = "m5d.12xlarge"
    M5D_16XLARGE = "m5d.16xlarge"
    M5D_24XLARGE = "m5d.24xlarge"
    M5D_METAL = "m5d.metal"
    M5DN_LARGE = "m5dn.large"
    M5DN_XLARGE = "m5dn.xlarge"
    M5DN_2XLARGE = "m5dn.2xlarge"
    M5DN_4XLARGE = "m5dn.4xlarge"
    M5DN_8XLARGE = "m5dn.8xlarge"
    M5DN_12XLARGE = "m5dn.12xlarge"
    M5DN_16XLARGE = "m5dn.16xlarge"
    M5DN_24XLARGE = "m5dn.24xlarge"
    M5N_LARGE = "m5n.large"
    M5N_XLARGE = "m5n.xlarge"
    M5N_2XLARGE = "m5n.2xlarge"
    M5N_4XLARGE = "m5n.4xlarge"
    M5N_8XLARGE = "m5n.8xlarge"
    M5N_12XLARGE = "m5n.12xlarge"
    M5N_16XLARGE = "m5n.16xlarge"
    M5N_24XLARGE = "m5n.24xlarge"
    M5ZN_LARGE = "m5zn.large"
    M5ZN_XLARGE = "m5zn.xlarge"
    M5ZN_2XLARGE = "m5zn.2xlarge"
    M5ZN_3XLARGE = "m5zn.3xlarge"
    M5ZN_6XLARGE = "m5zn.6xlarge"
    M5ZN_12XLARGE = "m5zn.12xlarge"
    M5ZN_METAL = "m5zn.metal"
    M6A_LARGE = "m6a.large"
    M6A_XLARGE = "m6a.xlarge"
    M6A_2XLARGE = "m6a.2xlarge"
    M6A_4XLARGE = "m6a.4xlarge"
    M6A_8XLARGE = "m6a.8xlarge"
    M6A_12XLARGE = "m6a.12xlarge"
    M6A_16XLARGE = "m6a.16xlarge"
    M6A_24XLARGE = "m6a.24xlarge"
    M6A_32XLARGE = "m6a.32xlarge"
    M6A_48XLARGE = "m6a.48xlarge"
    M6G_MEDIUM = "m6g.medium"
    M6G_LARGE = "m6g.large"
    M6G_XLARGE = "m6g.xlarge"
    M6G_2XLARGE = "m6g.2xlarge"
    M6G_4XLARGE = "m6g.4xlarge"
    M6G_8XLARGE = "m6g.8xlarge"
    M6G_12XLARGE = "m6g.12xlarge"
    M6G_16XLARGE = "m6g.16xlarge"
    M6GD_MEDIUM = "m6gd.medium"
    M6GD_LARGE = "m6gd.large"
    M6GD_XLARGE = "m6gd.xlarge"
    M6GD_2XLARGE = "m6gd.2xlarge"
    M6GD_4XLARGE = "m6gd.4xlarge"
    M6GD_8XLARGE = "m6gd.8xlarge"
    M6GD_12XLARGE = "m6gd.12xlarge"
    M6GD_16XLARGE = "m6gd.16xlarge"
    M6I_LARGE = "m6i.large"
    M6I_XLARGE = "m6i.xlarge"
    M6I_2XLARGE = "m6i.2xlarge"
    M6I_4XLARGE = "m6i.4xlarge"
    M6I_8XLARGE = "m6i.8xlarge"
    M6I_12XLARGE = "m6i.12xlarge"
    M6I_16XLARGE = "m6i.16xlarge"
    M6I_24XLARGE = "m6i.24xlarge"
    M6I_32XLARGE = "m6i.32xlarge"
    M6I_METAL = "m6i.metal"
    M6ID_LARGE = "m6id.large"
    M6ID_XLARGE = "m6id.xlarge"
    M6ID_2XLARGE = "m6id.2xlarge"
    M6ID_4XLARGE = "m6id.4xlarge"
    M6ID_8XLARGE = "m6id.8xlarge"
    M6ID_12XLARGE = "m6id.12xlarge"
    M6ID_16XLARGE = "m6id.16xlarge"
    M6ID_24XLARGE = "m6id.24xlarge"
    M6ID_32XLARGE = "m6id.32xlarge"
    M6ID_METAL = "m6id.metal"
    M6IN_LARGE = "m6in.large"
    M6IN_XLARGE = "m6in.xlarge"
    M6IN_2XLARGE = "m6in.2xlarge"
    M6IN_4XLARGE = "m6in.4xlarge"
    M6IN_8XLARGE = "m6in.8xlarge"
    M6IN_12XLARGE = "m6in.12xlarge"
    M6IN_16XLARGE = "m6in.16xlarge"
    M6IN_24XLARGE = "m6in.24xlarge"
    M6IN_32XLARGE = "m6in.32xlarge"
    M6IN_METAL = "m6in.metal"
    M6IDN_LARGE = "m6idn.large"
    M6IDN_XLARGE = "m6idn.xlarge"
    M6IDN_2XLARGE = "m6idn.2xlarge"
    M6IDN_4XLARGE = "m6idn.4xlarge"
    M6IDN_8XLARGE = "m6idn.8xlarge"
    M6IDN_12XLARGE = "m6idn.12xlarge"
    M6IDN_16XLARGE = "m6idn.16xlarge"
    M6IDN_24XLARGE = "m6idn.24xlarge"
    M6IDN_32XLARGE = "m6idn.32xlarge"
    M6IDN_METAL = "m6idn.metal"
    MAC1_METAL = "mac1.metal"
    MAC2_METAL = "mac2.metal"
    P2_XLARGE = "p2.xlarge"
    P2_8XLARGE = "p2.8xlarge"
    P2_16XLARGE = "p2.16xlarge"
    P3_2XLARGE = "p3.2xlarge"
    P3_8XLARGE = "p3.8xlarge"
    P3_16XLARGE = "p3.16xlarge"
    P3DN_24XLARGE = "p3dn.24xlarge"
    P4DE_24XLARGE = "p4de.24xlarge"
    P4D_24XLARGE = "p4d.24xlarge"
    R3_LARGE = "r3.large"
    R3_XLARGE = "r3.xlarge"
    R3_2XLARGE = "r3.2xlarge"
    R3_4XLARGE = "r3.4xlarge"
    R3_8XLARGE = "r3.8xlarge"
    R4_LARGE = "r4.large"
    R4_XLARGE = "r4.xlarge"
    R4_2XLARGE = "r4.2xlarge"
    R4_4XLARGE = "r4.4xlarge"
    R4_8XLARGE = "r4.8xlarge"
    R4_16XLARGE = "r4.16xlarge"
    R5_LARGE = "r5.large"
    R5_XLARGE = "r5.xlarge"
    R5_2XLARGE = "r5.2xlarge"
    R5_4XLARGE = "r5.4xlarge"
    R5_8XLARGE = "r5.8xlarge"
    R5_12XLARGE = "r5.12xlarge"
    R5_16XLARGE = "r5.16xlarge"
    R5_24XLARGE = "r5.24xlarge"
    R5_METAL = "r5.metal"
    R5A_LARGE = "r5a.large"
    R5A_XLARGE = "r5a.xlarge"
    R5A_2XLARGE = "r5a.2xlarge"
    R5A_4XLARGE = "r5a.4xlarge"
    R5A_8XLARGE = "r5a.8xlarge"
    R5A_12XLARGE = "r5a.12xlarge"
    R5A_16XLARGE = "r5a.16xlarge"
    R5A_24XLARGE = "r5a.24xlarge"
    R5AD_LARGE = "r5ad.large"
    R5AD_XLARGE = "r5ad.xlarge"
    R5AD_2XLARGE = "r5ad.2xlarge"
    R5AD_4XLARGE = "r5ad.4xlarge"
    R5AD_8XLARGE = "r5ad.8xlarge"
    R5AD_12XLARGE = "r5ad.12xlarge"
    R5AD_16XLARGE = "r5ad.16xlarge"
    R5AD_24XLARGE = "r5ad.24xlarge"
    R5B_LARGE = "r5b.large"
    R5B_XLARGE = "r5b.xlarge"
    R5B_2XLARGE = "r5b.2xlarge"
    R5B_4XLARGE = "r5b.4xlarge"
    R5B_8XLARGE = "r5b.8xlarge"
    R5B_12XLARGE = "r5b.12xlarge"
    R5B_16XLARGE = "r5b.16xlarge"
    R5B_24XLARGE = "r5b.24xlarge"
    R5B_METAL = "r5b.metal"
    R5D_LARGE = "r5d.large"
    R5D_XLARGE = "r5d.xlarge"
    R5D_2XLARGE = "r5d.2xlarge"
    R5D_4XLARGE = "r5d.4xlarge"
    R5D_8XLARGE = "r5d.8xlarge"
    R5D_12XLARGE = "r5d.12xlarge"
    R5D_16XLARGE = "r5d.16xlarge"
    R5D_24XLARGE = "r5d.24xlarge"
    R5D_METAL = "r5d.metal"
    R5DN_LARGE = "r5dn.large"
    R5DN_XLARGE = "r5dn.xlarge"
    R5DN_2XLARGE = "r5dn.2xlarge"
    R5DN_4XLARGE = "r5dn.4xlarge"
    R5DN_8XLARGE = "r5dn.8xlarge"
    R5DN_12XLARGE = "r5dn.12xlarge"
    R5DN_16XLARGE = "r5dn.16xlarge"
    R5DN_24XLARGE = "r5dn.24xlarge"
    R5N_LARGE = "r5n.large"
    R5N_XLARGE = "r5n.xlarge"
    R5N_2XLARGE = "r5n.2xlarge"
    R5N_4XLARGE = "r5n.4xlarge"
    R5N_8XLARGE = "r5n.8xlarge"
    R5N_12XLARGE = "r5n.12xlarge"
    R5N_16XLARGE = "r5n.16xlarge"
    R5N_24XLARGE = "r5n.24xlarge"
    R6A_LARGE = "r6a.large"
    R6A_XLARGE = "r6a.xlarge"
    R6A_2XLARGE = "r6a.2xlarge"
    R6A_4XLARGE = "r6a.4xlarge"
    R6A_8XLARGE = "r6a.8xlarge"
    R6A_12XLARGE = "r6a.12xlarge"
    R6A_16XLARGE = "r6a.16xlarge"
    R6A_24XLARGE = "r6a.24xlarge"
    R6A_32XLARGE = "r6a.32xlarge"
    R6A_48XLARGE = "r6a.48xlarge"
    R6G_MEDIUM = "r6g.medium"
    R6G_LARGE = "r6g.large"
    R6G_XLARGE = "r6g.xlarge"
    R6G_2XLARGE = "r6g.2xlarge"
    R6G_4XLARGE = "r6g.4xlarge"
    R6G_8XLARGE = "r6g.8xlarge"
    R6G_12XLARGE = "r6g.12xlarge"
    R6G_16XLARGE = "r6g.16xlarge"
    R6GD_MEDIUM = "r6gd.medium"
    R6GD_LARGE = "r6gd.large"
    R6GD_XLARGE = "r6gd.xlarge"
    R6GD_2XLARGE = "r6gd.2xlarge"
    R6GD_4XLARGE = "r6gd.4xlarge"
    R6GD_8XLARGE = "r6gd.8xlarge"
    R6GD_12XLARGE = "r6gd.12xlarge"
    R6GD_16XLARGE = "r6gd.16xlarge"
    R6I_LARGE = "r6i.large"
    R6I_XLARGE = "r6i.xlarge"
    R6I_2XLARGE = "r6i.2xlarge"
    R6I_4XLARGE = "r6i.4xlarge"
    R6I_8XLARGE = "r6i.8xlarge"
    R6I_12XLARGE = "r6i.12xlarge"
    R6I_16XLARGE = "r6i.16xlarge"
    R6I_24XLARGE = "r6i.24xlarge"
    R6I_32XLARGE = "r6i.32xlarge"
    R6I_METAL = "r6i.metal"
    R6ID_LARGE = "r6id.large"
    R6ID_XLARGE = "r6id.xlarge"
    R6ID_2XLARGE = "r6id.2xlarge"
    R6ID_4XLARGE = "r6id.4xlarge"
    R6ID_8XLARGE = "r6id.8xlarge"
    R6ID_12XLARGE = "r6id.12xlarge"
    R6ID_16XLARGE = "r6id.16xlarge"
    R6ID_24XLARGE = "r6id.24xlarge"
    R6ID_32XLARGE = "r6id.32xlarge"
    R6ID_METAL = "r6id.metal"
    R6IN_LARGE = "r6in.large"
    R6IN_XLARGE = "r6in.xlarge"
    R6IN_2XLARGE = "r6in.2xlarge"
    R6IN_4XLARGE = "r6in.4xlarge"
    R6IN_8XLARGE = "r6in.8xlarge"
    R6IN_12XLARGE = "r6in.12xlarge"
    R6IN_16XLARGE = "r6in.16xlarge"
    R6IN_24XLARGE = "r6in.24xlarge"
    R6IN_32XLARGE = "r6in.32xlarge"
    R6IN_METAL = "r6in.metal"
    R6IDN_LARGE = "r6idn.large"
    R6IDN_XLARGE = "r6idn.xlarge"
    R6IDN_2XLARGE = "r6idn.2xlarge"
    R6IDN_4XLARGE = "r6idn.4xlarge"
    R6IDN_8XLARGE = "r6idn.8xlarge"
    R6IDN_12XLARGE = "r6idn.12xlarge"
    R6IDN_16XLARGE = "r6idn.16xlarge"
    R6IDN_24XLARGE = "r6idn.24xlarge"
    R6IDN_32XLARGE = "r6idn.32xlarge"
    R6IDN_METAL = "r6idn.metal"
    T2_NANO = "t2.nano"
    T2_MICRO = "t2.micro"
    T2_SMALL = "t2.small"
    T2_MEDIUM = "t2.medium"
    T2_LARGE = "t2.large"
    T2_XLARGE = "t2.xlarge"
    T2_2XLARGE = "t2.2xlarge"
    T3_NANO = "t3.nano"
    T3_MICRO = "t3.micro"
    T3_SMALL = "t3.small"
    T3_MEDIUM = "t3.medium"
    T3_LARGE = "t3.large"
    T3_XLARGE = "t3.xlarge"
    T3_2XLARGE = "t3.2xlarge"
    T3A_NANO = "t3a.nano"
    T3A_MICRO = "t3a.micro"
    T3A_SMALL = "t3a.small"
    T3A_MEDIUM = "t3a.medium"
    T3A_LARGE = "t3a.large"
    T3A_XLARGE = "t3a.xlarge"
    T3A_2XLARGE = "t3a.2xlarge"
    T4G_NANO = "t4g.nano"
    T4G_MICRO = "t4g.micro"
    T4G_SMALL = "t4g.small"
    T4G_MEDIUM = "t4g.medium"
    T4G_LARGE = "t4g.large"
    T4G_XLARGE = "t4g.xlarge"
    T4G_2XLARGE = "t4g.2xlarge"
    U_3TB1_METAL = "u-3tb1.metal"
    U_6TB1_METAL = "u-6tb1.metal"
    U_6TB1_56XLARGE = "u-6tb1.56xlarge"
    U_9TB1_METAL = "u-9tb1.metal"
    U_12TB1_METAL = "u-12tb1.metal"
    VT1_3XLARGE = "vt1.3xlarge"
    VT1_6XLARGE = "vt1.6xlarge"
    VT1_24XLARGE = "vt1.24xlarge"
    X1_16XLARGE = "x1.16xlarge"
    X1_32XLARGE = "x1.32xlarge"
    X1E_XLARGE = "x1e.xlarge"
    X1E_2XLARGE = "x1e.2xlarge"
    X1E_4XLARGE = "x1e.4xlarge"
    X1E_8XLARGE = "x1e.8xlarge"
    X1E_16XLARGE = "x1e.16xlarge"
    X1E_32XLARGE = "x1e.32xlarge"
    X2IDN_16XLARGE = "x2idn.16xlarge"
    X2IDN_24XLARGE = "x2idn.24xlarge"
    X2IDN_32XLARGE = "x2idn.32xlarge"
    X2IDN_METAL = "x2idn.metal"
    X2IEDN_XLARGE = "x2iedn.xlarge"
    X2IEDN_2XLARGE = "x2iedn.2xlarge"
    X2IEDN_4XLARGE = "x2iedn.4xlarge"
    X2IEDN_8XLARGE = "x2iedn.8xlarge"
    X2IEDN_16XLARGE = "x2iedn.16xlarge"
    X2IEDN_24XLARGE = "x2iedn.24xlarge"
    X2IEDN_32XLARGE = "x2iedn.32xlarge"
    X2IEDN_METAL = "x2iedn.metal"
    X2IEZN_2XLARGE = "x2iezn.2xlarge"
    X2IEZN_4XLARGE = "x2iezn.4xlarge"
    X2IEZN_6XLARGE = "x2iezn.6xlarge"
    X2IEZN_8XLARGE = "x2iezn.8xlarge"
    X2IEZN_12XLARGE = "x2iezn.12xlarge"
    X2IEZN_METAL = "x2iezn.metal"
    Z1D_LARGE = "z1d.large"
    Z1D_XLARGE = "z1d.xlarge"
    Z1D_2XLARGE = "z1d.2xlarge"
    Z1D_3XLARGE = "z1d.3xlarge"
    Z1D_6XLARGE = "z1d.6xlarge"
    Z1D_12XLARGE = "z1d.12xlarge"
    Z1D_METAL = "z1d.metal"

    @staticmethod
    def of(value: str):
        if value:
            return EC2InstanceType(value)
        return None


class EC2InstanceState(Enum):
    PENDING = "pending"
    RUNNING = "running"
    SHUTTING_DOWN = "shutting-down"
    TERMINATED = "terminated"
    STOPPING = "stopping"
    STOPPED = "stopped"

    @staticmethod
    def of(value: str):
        if value:
            return EC2InstanceState(value)
        return None
