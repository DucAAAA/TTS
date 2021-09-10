from dataclasses import dataclass, field
from typing import List

from TTS.tts.configs.shared_configs import BaseTTSConfig
from TTS.tts.models.forward_tts import ForwardTTSArgs


@dataclass
class FastPitchConfig(BaseTTSConfig):
    """Configure `ForwardTTS` as FastPitch model.

    Example:

        >>> from TTS.tts.configs import FastPitchConfig
        >>> config = FastPitchConfig()

    Args:
        model (str):
            Model name used for selecting the right model at initialization. Defaults to `fast_pitch`.

        model_args (Coqpit):
            Model class arguments. Check `FastPitchArgs` for more details. Defaults to `FastPitchArgs()`.

        data_dep_init_steps (int):
            Number of steps used for computing normalization parameters at the beginning of the training. GlowTTS uses
            Activation Normalization that pre-computes normalization stats at the beginning and use the same values
            for the rest. Defaults to 10.

        use_speaker_embedding (bool):
            enable / disable using speaker embeddings for multi-speaker models. If set True, the model is
            in the multi-speaker mode. Defaults to False.

        use_d_vector_file (bool):
            enable /disable using external speaker embeddings in place of the learned embeddings. Defaults to False.

        d_vector_file (str):
            Path to the file including pre-computed speaker embeddings. Defaults to None.

        d_vector_dim (int):
            Dimension of the external speaker embeddings. Defaults to 0.

        optimizer (str):
            Name of the model optimizer. Defaults to `Adam`.

        optimizer_params (dict):
            Arguments of the model optimizer. Defaults to `{"betas": [0.9, 0.998], "weight_decay": 1e-6}`.

        lr_scheduler (str):
            Name of the learning rate scheduler. Defaults to `Noam`.

        lr_scheduler_params (dict):
            Arguments of the learning rate scheduler. Defaults to `{"warmup_steps": 4000}`.

        lr (float):
            Initial learning rate. Defaults to `1e-3`.

        grad_clip (float):
            Gradient norm clipping value. Defaults to `5.0`.

        spec_loss_type (str):
            Type of the spectrogram loss. Check `ForwardTTSLoss` for possible values. Defaults to `mse`.

        duration_loss_type (str):
            Type of the duration loss. Check `ForwardTTSLoss` for possible values. Defaults to `mse`.

        use_ssim_loss (bool):
            Enable/disable the use of SSIM (Structural Similarity) loss. Defaults to True.

        wd (float):
            Weight decay coefficient. Defaults to `1e-7`.

        ssim_loss_alpha (float):
            Weight for the SSIM loss. If set 0, disables the SSIM loss. Defaults to 1.0.

        dur_loss_alpha (float):
            Weight for the duration predictor's loss. If set 0, disables the huber loss. Defaults to 1.0.

        spec_loss_alpha (float):
            Weight for the L1 spectrogram loss. If set 0, disables the L1 loss. Defaults to 1.0.

        pitch_loss_alpha (float):
            Weight for the pitch predictor's loss. If set 0, disables the pitch predictor. Defaults to 1.0.

        binary_loss_alpha (float):
            Weight for the binary loss. If set 0, disables the binary loss. Defaults to 1.0.

        binary_align_loss_start_step (int):
            Start binary alignment loss after this many steps. Defaults to 20000.

        min_seq_len (int):
            Minimum input sequence length to be used at training.

        max_seq_len (int):
            Maximum input sequence length to be used at training. Larger values result in more VRAM usage.
    """

    model: str = "forward_tts"
    # model specific params
    model_args: ForwardTTSArgs = field(default_factory=ForwardTTSArgs)

    # multi-speaker settings
    use_speaker_embedding: bool = False
    use_d_vector_file: bool = False
    d_vector_file: str = False
    d_vector_dim: int = 0

    # optimizer parameters
    optimizer: str = "Adam"
    optimizer_params: dict = field(default_factory=lambda: {"betas": [0.9, 0.998], "weight_decay": 1e-6})
    lr_scheduler: str = "NoamLR"
    lr_scheduler_params: dict = field(default_factory=lambda: {"warmup_steps": 4000})
    lr: float = 1e-4
    grad_clip: float = 5.0

    # loss params
    spec_loss_type: str = "mse"
    duration_loss_type: str = "mse"
    use_ssim_loss: bool = True
    ssim_loss_alpha: float = 1.0
    dur_loss_alpha: float = 1.0
    spec_loss_alpha: float = 1.0
    pitch_loss_alpha: float = 1.0
    aligner_loss_alpha: float = 1.0
    binary_align_loss_alpha: float = 1.0
    binary_align_loss_start_step: int = 20000

    # overrides
    min_seq_len: int = 13
    max_seq_len: int = 200
    r: int = 1  # DO NOT CHANGE

    # dataset configs
    compute_f0: bool = True
    f0_cache_path: str = None

    # testing
    test_sentences: List[str] = field(
        default_factory=lambda: [
            "It took me quite a long time to develop a voice, and now that I have it I'm not going to be silent.",
            "Be a voice, not an echo.",
            "I'm sorry Dave. I'm afraid I can't do that.",
            "This cake is great. It's so delicious and moist.",
            "Prior to November 22, 1963.",
        ]
    )
