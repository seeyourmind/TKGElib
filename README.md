<h1 align="center">ECEformer</h1>
<h5 align="center">Transformer-based Reasoning for Learning Evolutionary Chain of Events on Temporal Knowledge Graph</h5>

ECEformer is a novel Transformer-based reasoning model for TKG to learn the Evolutionary Chain of Events. It will appear in SIGIR 2024 ([arXiv version](https://arxiv.org/abs/2405.00352)).

## Installation

The repo requires python>=3.7, anaconda and a new env is recommended.

``` sh
conda create -n eceformer python=3.7 -y # optional
conda activate eceformer # optional
git clone git@github.com:seeyourmind/TKGElib.git
cd ECEformer
pip install -e .
```

### Data

First download the standard benchmark datasets. The Data folder can be downloaded from [GDELT & ICEWS14/05-15](https://github.com/BorealisAI/de-simple/tree/master/datasets), [ICEWS18](https://github.com/TemporalKGTeam/xERTE/tree/main/tKGR/data/ICEWS18_forecasting), [YAGO11k & WikiData12k](https://drive.google.com/open?id=1S0dcMDXVZp8CFSCMojkBQI1gCva8Dm-0). Then process the dataset using the commands below.

```sh
cd data
# for GDELT/ICEWS14/ICEWS05-15/ICEWS18
# e.g. python preprocess.py icews14
python preprocess.py $dataset_name
# for YAGO11k and WikiData12k
python preprocess_intravel.py $dataset_name
```

### Training

Configurations for the experiments are in the `/config` folder.

``` sh
python -m kge start config/gdelt-best.yaml
```

The training process uses DataParallel in all visible GPUs by default, which can be overrode by appending `--job.device cpu` to the command above.

### Evaluation

You can evaluate the trained models on dev/test set using the following commands.

``` sh
python -m kge eval <saved_dir>
python -m kge test <saved_dir>
```

## Acknowledgment

Thanks [LibKGE](https://github.com/uma-pi1/kge) and [HittER](https://github.com/microsoft/HittER) for providing the preprocessing scripts and the base frameworks.

## Citation

```
@inproceedings{fang-sigir-2024-eceformer,
    title = "Temporal Knowledge Graph Completion, Context Information Mining, Link Prediction, Evolutionary Chain of Event",
    author = "Fang, Zhiyu and Lei, Shuai-Long and Zhu, Xiaobin and Yang, Chun and Zhang, Shi-Xue and Yin, Xu-Cheng and Qin, Jingyan",
    booktitle = "Proceedings of The 47th International ACM SIGIR Conference",
    year = "2024"
}
```
