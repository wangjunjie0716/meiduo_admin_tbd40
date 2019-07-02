from rest_framework import serializers

from goods.models import SKU


class SkuSpecSerializer(serializers.Serializer):
    spec_id = serializers.IntegerField()
    option_id = serializers.IntegerField()


class SkuModelSerializer(serializers.ModelSerializer):
    # 外键对应的隐藏属性需要明确定义
    spu_id = serializers.IntegerField()
    category_id = serializers.IntegerField()
    # 关系属性默认输出主键，指定输出字符串
    spu = serializers.StringRelatedField(read_only=True)
    category = serializers.StringRelatedField(read_only=True)
    # 隐藏的关系属性：specs，表示库存商品的规格选项信息
    specs = SkuSpecSerializer(many=True, read_only=True)

    class Meta:
        model = SKU
        fields = '__all__'