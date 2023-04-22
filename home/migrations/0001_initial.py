# Generated by Django 2.2.10 on 2020-06-07 19:33
# ruff: noqa: E501

import django.db.models.deletion
import machina.apps.forum_conversation.forum_polls.models
import wagtail.contrib.table_block.blocks
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.documents.blocks
import wagtail.images.blocks
import wagtail.snippets.blocks
from django.db import migrations, models

import home.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
        ('puput', '0005_blogpage_main_color'),
    ]

    operations = [
        migrations.CreateModel(
            name='Advert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('url', models.URLField(blank=True, null=True)),
                ('body', wagtail.core.fields.RichTextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='FullWidthPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('repeat_in_subnav', models.BooleanField(default=False, help_text="If checked, a link to this page will be repeated alongside it's direct children when displaying a sub-navigation for this page.", verbose_name='repeat in sub-navigation')),
                ('repeated_item_text', models.CharField(blank=True, help_text="e.g. 'Section home' or 'Overview'. If left blank, the page title will be used.", max_length=255, verbose_name='repeated item link text')),
                ('body', wagtail.core.fields.StreamField([('h2', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('h3', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('h4', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('intro', wagtail.core.blocks.RichTextBlock(icon='pilcrow')), ('paragraph', wagtail.core.blocks.RichTextBlock(icon='pilcrow')), ('aligned_image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('caption', wagtail.core.blocks.RichTextBlock(blank=True, null=True, required=False)), ('alignment', home.models.ImageFormatChoiceBlock()), ('width', wagtail.core.blocks.IntegerBlock(blank=True, default=None, help_text='optional width in px. Default is auto.', null=True, required=False))], icon='image', label='Aligned image')), ('pullquote', wagtail.core.blocks.StructBlock([('quote', wagtail.core.blocks.TextBlock('quote title')), ('attribution', wagtail.core.blocks.CharBlock())])), ('aligned_html', wagtail.core.blocks.StructBlock([('html', wagtail.core.blocks.RawHTMLBlock()), ('alignment', home.models.HTMLAlignmentChoiceBlock())], icon='code', label='Raw HTML')), ('document', wagtail.documents.blocks.DocumentChooserBlock(icon='doc-full-inverse')), ('wgo', wagtail.core.blocks.StructBlock([('sgf', wagtail.documents.blocks.DocumentChooserBlock()), ('alignment', home.models.WgoAlignmentChoiceBlock()), ('width', wagtail.core.blocks.IntegerBlock(default=700))], label='wgo')), ('table', wagtail.contrib.table_block.blocks.TableBlock()), ('poll', wagtail.snippets.blocks.SnippetChooserBlock(machina.apps.forum_conversation.forum_polls.models.TopicPoll, template='home/includes/poll.html'))], blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page', models.Model),
        ),
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='LeftSidebarPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('repeat_in_subnav', models.BooleanField(default=False, help_text="If checked, a link to this page will be repeated alongside it's direct children when displaying a sub-navigation for this page.", verbose_name='repeat in sub-navigation')),
                ('repeated_item_text', models.CharField(blank=True, help_text="e.g. 'Section home' or 'Overview'. If left blank, the page title will be used.", max_length=255, verbose_name='repeated item link text')),
                ('body', wagtail.core.fields.StreamField([('h2', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('h3', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('h4', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('intro', wagtail.core.blocks.RichTextBlock(icon='pilcrow')), ('paragraph', wagtail.core.blocks.RichTextBlock(icon='pilcrow')), ('aligned_image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('caption', wagtail.core.blocks.RichTextBlock(blank=True, null=True, required=False)), ('alignment', home.models.ImageFormatChoiceBlock()), ('width', wagtail.core.blocks.IntegerBlock(blank=True, default=None, help_text='optional width in px. Default is auto.', null=True, required=False))], icon='image', label='Aligned image')), ('pullquote', wagtail.core.blocks.StructBlock([('quote', wagtail.core.blocks.TextBlock('quote title')), ('attribution', wagtail.core.blocks.CharBlock())])), ('aligned_html', wagtail.core.blocks.StructBlock([('html', wagtail.core.blocks.RawHTMLBlock()), ('alignment', home.models.HTMLAlignmentChoiceBlock())], icon='code', label='Raw HTML')), ('document', wagtail.documents.blocks.DocumentChooserBlock(icon='doc-full-inverse')), ('wgo', wagtail.core.blocks.StructBlock([('sgf', wagtail.documents.blocks.DocumentChooserBlock()), ('alignment', home.models.WgoAlignmentChoiceBlock()), ('width', wagtail.core.blocks.IntegerBlock(default=700))], label='wgo')), ('table', wagtail.contrib.table_block.blocks.TableBlock()), ('poll', wagtail.snippets.blocks.SnippetChooserBlock(machina.apps.forum_conversation.forum_polls.models.TopicPoll, template='home/includes/poll.html'))], blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page', models.Model),
        ),
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True, max_length=100, null=True)),
                ('source', models.TextField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='RightSidebarPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('repeat_in_subnav', models.BooleanField(default=False, help_text="If checked, a link to this page will be repeated alongside it's direct children when displaying a sub-navigation for this page.", verbose_name='repeat in sub-navigation')),
                ('repeated_item_text', models.CharField(blank=True, help_text="e.g. 'Section home' or 'Overview'. If left blank, the page title will be used.", max_length=255, verbose_name='repeated item link text')),
                ('body', wagtail.core.fields.StreamField([('h2', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('h3', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('h4', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('intro', wagtail.core.blocks.RichTextBlock(icon='pilcrow')), ('paragraph', wagtail.core.blocks.RichTextBlock(icon='pilcrow')), ('aligned_image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('caption', wagtail.core.blocks.RichTextBlock(blank=True, null=True, required=False)), ('alignment', home.models.ImageFormatChoiceBlock()), ('width', wagtail.core.blocks.IntegerBlock(blank=True, default=None, help_text='optional width in px. Default is auto.', null=True, required=False))], icon='image', label='Aligned image')), ('pullquote', wagtail.core.blocks.StructBlock([('quote', wagtail.core.blocks.TextBlock('quote title')), ('attribution', wagtail.core.blocks.CharBlock())])), ('aligned_html', wagtail.core.blocks.StructBlock([('html', wagtail.core.blocks.RawHTMLBlock()), ('alignment', home.models.HTMLAlignmentChoiceBlock())], icon='code', label='Raw HTML')), ('document', wagtail.documents.blocks.DocumentChooserBlock(icon='doc-full-inverse')), ('wgo', wagtail.core.blocks.StructBlock([('sgf', wagtail.documents.blocks.DocumentChooserBlock()), ('alignment', home.models.WgoAlignmentChoiceBlock()), ('width', wagtail.core.blocks.IntegerBlock(default=700))], label='wgo')), ('table', wagtail.contrib.table_block.blocks.TableBlock()), ('poll', wagtail.snippets.blocks.SnippetChooserBlock(machina.apps.forum_conversation.forum_polls.models.TopicPoll, template='home/includes/poll.html'))], blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page', models.Model),
        ),
        migrations.CreateModel(
            name='StreamFieldEntryPage',
            fields=[
                ('entrypage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='puput.EntryPage')),
                ('streamfield', wagtail.core.fields.StreamField([('h2', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('h3', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('h4', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('intro', wagtail.core.blocks.RichTextBlock(icon='pilcrow')), ('paragraph', wagtail.core.blocks.RichTextBlock(icon='pilcrow')), ('aligned_image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('caption', wagtail.core.blocks.RichTextBlock(blank=True, null=True, required=False)), ('alignment', home.models.ImageFormatChoiceBlock()), ('width', wagtail.core.blocks.IntegerBlock(blank=True, default=None, help_text='optional width in px. Default is auto.', null=True, required=False))], icon='image', label='Aligned image')), ('pullquote', wagtail.core.blocks.StructBlock([('quote', wagtail.core.blocks.TextBlock('quote title')), ('attribution', wagtail.core.blocks.CharBlock())])), ('aligned_html', wagtail.core.blocks.StructBlock([('html', wagtail.core.blocks.RawHTMLBlock()), ('alignment', home.models.HTMLAlignmentChoiceBlock())], icon='code', label='Raw HTML')), ('document', wagtail.documents.blocks.DocumentChooserBlock(icon='doc-full-inverse')), ('wgo', wagtail.core.blocks.StructBlock([('sgf', wagtail.documents.blocks.DocumentChooserBlock()), ('alignment', home.models.WgoAlignmentChoiceBlock()), ('width', wagtail.core.blocks.IntegerBlock(default=700))], label='wgo')), ('table', wagtail.contrib.table_block.blocks.TableBlock()), ('poll', wagtail.snippets.blocks.SnippetChooserBlock(machina.apps.forum_conversation.forum_polls.models.TopicPoll, template='home/includes/poll.html'))], blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('puput.entrypage',),
        ),
    ]
