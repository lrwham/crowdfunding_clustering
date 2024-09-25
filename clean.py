"""
# Data Cleaning
Since the dataset includes foreign language, a first step is renaming columns and translating some features.
## Column Names and Descriptions
The following was provided by the author on the UCI ML Repository. I've copied and pasted this below to facilitate use here.
1. id: The unique identifier of the project.
1. platform_adi: The crowdfunding platform where the project is hosted.
1. kitle_fonlamasi_turu: Type of crowdfunding (e.g., reward, donation).
1. kategori: Category of the project.
1. fon_sekli: Funding method (e.g., all or nothing).
1. proje_adi: Project name.
1. proje_sahibi: Name of the project owner.
1. proje_sahibi_cinsiyet: Gender of the project owner.
1. kac_proje_destekledi: Number of projects the owner has backed.
1. kac_projeye_abone: Number of projects the owner has subscribed to.
1. kac_projenin_sahibi: Number of projects owned by the project owner.
1. kac_proje_takiminda: Number of teams the project owner is part of.
1. konum: Location of the project owner.
1. bolge: Region of the project.
1. yil: Year the project was launched.
1. proje_baslama_tarihi: Start date of the project.
1. proje_bitis_tarihi: End date of the project.
1. gun_sayisi: Duration of the project in days.
1. tanitim_videosu: Whether the project has a promotional video.
1. video_uzunlugu: Length of the promotional video.
1. gorsel_sayisi: Number of images related to the project.
1. sss: Whether the project has a Frequently Asked Questions (FAQ) section.
1. guncellemeler: Number of updates for the project.
1. yorumlar: Number of comments on the project.
1. destekci_sayisi: Number of backers for the project.
1. odul_sayisi: Number of rewards offered in the project.
1. ekip_kisi_sayisi: Number of people in the project team.
1. web_sitesi: Whether the project has a website.
1. sosyal_medya: Whether the project has social media accounts.
1. sm_sayisi: Number of social media accounts for the project.
1. sm_takipci: Number of social media followers for the project.
1. etiket_sayisi: Number of tags used in the project description.
1. icerik_kelime_sayisi: Number of words in the project description.
1. proje_aciklamasi: Description of the project.
1. hedef_miktari: Target amount of funding for the project.
1. toplanan_tutar: Amount of funding collected for the project.
1. destek_orani: Percentage of the target amount achieved.
1. basari_durumu: Success status of the project (successful or unsuccessful).
"""
import pandas as pd

def translate_columns(dataframe: pd.DataFrame):
    new_columns = ["id","platform","crowdfunding_type","project_category","funding_method","project_name","project_owner_name","project_owner_gender","project_owner_n_backed","project_owner_n_subscribed","project_owner_n_owned","project_owner_n_teams","project_owner_location","project_region","year_launched","start_date","end_date","project_duration","has_video","video_length","n_images","has_faq","n_updates","n_comments","n_backers","n_rewards","n_team_members","has_website","has_social","n_social","n_followers","n_tags","description_wordcount","description",'funding_target',"funding_collected","percent_collected","success"]
    
    dataframe.columns = new_columns

def translate_project_categories(dataframe: pd.DataFrame):
    categories = [
        "diğer",
        "çevre",
        "dans-performans",
        "eğitim",
        "film-video-fotoğraf",
        "yayıncılık",
        "gıda-yeme-içme",
        "kültür-sanat",
        "müzik",
        "sağlık-güzellik",
        "spor",
        "moda",
        "teknoloji",
        "turizm",
        "hayvanlar",
        "tasarım",
        "sosyal sorumluluk",
    ]
    translated_categories = [
        "other",
        "environment",
        "dance-performance",
        "education",
        "film-video-photography",
        "publishing",
        "food-eating-drinking",
        "culture-art",
        "music",
        "health-beauty",
        "sports",
        "fashion",
        "technology",
        "tourism",
        "animals",
        "design",
        "social responsibility",
    ]

    category_dict = dict(zip(categories, translated_categories))

    dataframe['project_category'] = dataframe['project_category'].map(category_dict)

def translate_crowdfunding_type(dataframe: pd.DataFrame):
    crowdfunding_types = ['ödül', 'bağış']
    translated_crowdfunding_types = ['reward', 'donation']

    crowdfunding_type_dict = dict(zip(crowdfunding_types, translated_crowdfunding_types))

    dataframe['crowdfunding_type'] = dataframe['crowdfunding_type'].map(crowdfunding_type_dict)

def translate_funding_method(dataframe: pd.DataFrame):
    funding_methods = ['ya hep ya hiç','hepsi kalsın']
    translated_funding_methods = ['all or nothing','keep it all']

    funding_method_dict = dict(zip(funding_methods, translated_funding_methods))

    dataframe['funding_method'] = dataframe['funding_method'].map(funding_method_dict)

def translate_project_owner_gender(dataframe: pd.DataFrame):
    project_owner_gender = ['belirsiz','kadın','erkek']
    translated_project_owner_gender = ['indeterminate','woman','man']

    project_owner_gender_dict = dict(zip(project_owner_gender, translated_project_owner_gender))

    dataframe["project_owner_gender"] = dataframe["project_owner_gender"].map(project_owner_gender_dict)

def translate_project_success(dataframe: pd.DataFrame):
    success = ['başarılı','başarısız']
    translated_success = [1,0]

    success_dict = dict(zip(success, translated_success))

    dataframe["success"] = dataframe["success"].map(success_dict)

def translate_yes_no_columns(dataframe: pd.DataFrame):
    yes_no_columns = ['has_video','has_faq','has_website','has_social']
    turkish = ["yok","var"]
    english = ["no","yes"]
    yes_no_dict = dict(zip(turkish,english))
    for column in yes_no_columns:
        dataframe[column] = dataframe[column].map(yes_no_dict)

def translate_all(dataframe: pd.DataFrame):
    translate_columns(dataframe)
    translate_project_categories(dataframe)
    translate_crowdfunding_type(dataframe)
    translate_funding_method(dataframe)
    translate_project_owner_gender(dataframe)
    translate_project_success(dataframe)
    translate_yes_no_columns(dataframe)

def fix_percent_column(dataframe: pd.DataFrame):
    dataframe["percent_collected"] = dataframe["percent_collected"].str.replace("%","").astype(float)

def save_translated_data(dataframe: pd.DataFrame, path: str):
    dataframe.to_csv(path, index=False, sep=";")

if __name__ == "__main__":
    data = pd.read_csv("turkishCF.csv", sep=";")
    translate_all(data)
    fix_percent_column(data)
    save_translated_data(data, "translated_data.csv")