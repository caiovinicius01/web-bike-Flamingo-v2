# Generated by Django 3.1.3 on 2020-11-21 02:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0003_auto_20201119_0400'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bicicleta',
            fields=[
                ('produto_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='loja.produto')),
                ('modelo', models.CharField(max_length=60, null=True, verbose_name='Modelo')),
            ],
            bases=('loja.produto',),
        ),
        migrations.AddField(
            model_name='produto',
            name='marca',
            field=models.CharField(max_length=40, null=True, verbose_name='Marca'),
        ),
        migrations.AlterField(
            model_name='endereco',
            name='cidade',
            field=models.CharField(max_length=30, null=True, verbose_name='Cidade'),
        ),
        migrations.AlterField(
            model_name='endereco',
            name='complemento',
            field=models.CharField(max_length=50, null=True, verbose_name='Complemento'),
        ),
        migrations.AlterField(
            model_name='endereco',
            name='estado',
            field=models.CharField(max_length=2, null=True, verbose_name='Estado'),
        ),
        migrations.AlterField(
            model_name='endereco',
            name='logradouro',
            field=models.CharField(max_length=60, null=True, verbose_name='Endereço'),
        ),
        migrations.AlterField(
            model_name='endereco',
            name='numero',
            field=models.CharField(max_length=10, null=True, verbose_name='Número'),
        ),
        migrations.AlterField(
            model_name='endereco',
            name='pais',
            field=models.CharField(max_length=30, null=True, verbose_name='País'),
        ),
        migrations.AlterField(
            model_name='iteminventario',
            name='codigo',
            field=models.CharField(max_length=12, null=True, verbose_name='Código'),
        ),
        migrations.AlterField(
            model_name='iteminventario',
            name='quantidadeEmEstoque',
            field=models.PositiveIntegerField(null=True, verbose_name='Quantidade'),
        ),
        migrations.AlterField(
            model_name='pagamento',
            name='codigo',
            field=models.CharField(max_length=12, null=True, verbose_name='Código'),
        ),
        migrations.AlterField(
            model_name='pagamento',
            name='valorTotal',
            field=models.DecimalField(decimal_places=2, max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='parcelamento',
            name='codigo',
            field=models.CharField(max_length=12, null=True, verbose_name='Código'),
        ),
        migrations.AlterField(
            model_name='parcelamento',
            name='valorParcela',
            field=models.DecimalField(decimal_places=2, max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='data_do_pedido',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='produto',
            name='codigo',
            field=models.CharField(max_length=12, null=True, verbose_name='Código'),
        ),
        migrations.AlterField(
            model_name='produto',
            name='desconto',
            field=models.DecimalField(decimal_places=2, max_digits=4, null=True),
        ),
        migrations.AlterField(
            model_name='produto',
            name='descricao',
            field=models.CharField(max_length=144, null=True, verbose_name='Descrição do produto'),
        ),
        migrations.AlterField(
            model_name='produto',
            name='imagem',
            field=models.ImageField(default=None, null=True, upload_to='img'),
        ),
        migrations.AlterField(
            model_name='produto',
            name='preco',
            field=models.DecimalField(decimal_places=2, max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='telefone',
            name='numero',
            field=models.CharField(max_length=12, null=True, verbose_name='Número'),
        ),
        migrations.AlterField(
            model_name='telefone',
            name='tipo',
            field=models.CharField(choices=[('cel', 'celular'), ('res', 'residencial'), ('com', 'comercial')], max_length=3, null=True, verbose_name='Tipo do telefone'),
        ),
    ]
