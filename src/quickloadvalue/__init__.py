# coding: utf-8
#
#  事前処理が必要な変数読み込みの高速化(キャッシュ化)
#  
# Licence : MIT Licence
# owner   : Fumiya Shibamata
#

import os
import pickle

# 管理名、関数、管理ディレクトリパス
def get(modelName, loadFunction, type=1, dir="./model/"):
    """
    値の取得
        modelName : 保存するバイナリデータのファイル名
        loadFunction : キャッシュが無効の時に実行される取得処理
        type : 将来的に実装される強制読み込み条件（未指定か1を入れておけばmodelがないときのみ読み込み）
        dir : モデルデータを管理するディレクトリ(未指定時 ./ )
    """
    
    # ----------------------
    # キャッシュを利用していいか条件を満たしているか確認
    # ----------------------
    if os.path.isfile(dir + modelName + ".model"):
        # キャッシュの読み込み
        return_value = _load_dictionary(dir + modelName + ".model")
    else :
        # 値の取得
        return_value = loadFunction()
        # キャッシュの保存
        _save_dictionary(dir + modelName + ".model", return_value)
    return return_value

def _save_dictionary(file, values):
    """
    バイナリデータの保存
        file : 保存するバイナリデータのファイル名
    """
    f = open(file, 'wb')
    pickle.dump(values, f)
    f.close()

def _load_dictionary(file):
    """
    バイナリデータの読み込み
        file : 保存するバイナリデータのファイル名
    """
    f = open(file, 'rb')
    loadFile = pickle.load(f)
    f.close()
    return loadFile    
