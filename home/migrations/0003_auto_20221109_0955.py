# Generated by Django 3.1.14 on 2022-11-09 09:55
# ruff: noqa: E501

import machina.apps.forum_conversation.forum_polls.models
import wagtail.contrib.table_block.blocks
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.documents.blocks
import wagtail.images.blocks
import wagtail.snippets.blocks
from django.db import migrations

import home.models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_sponsor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fullwidthpage',
            name='body',
            field=wagtail.core.fields.StreamField([('h2', wagtail.core.blocks.CharBlock(form_classname='title', icon='title')), ('h3', wagtail.core.blocks.CharBlock(form_classname='title', icon='title')), ('h4', wagtail.core.blocks.CharBlock(form_classname='title', icon='title')), ('intro', wagtail.core.blocks.RichTextBlock(icon='pilcrow')), ('paragraph', wagtail.core.blocks.RichTextBlock(icon='pilcrow')), ('aligned_image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('caption', wagtail.core.blocks.RichTextBlock(blank=True, null=True, required=False)), ('alignment', home.models.ImageFormatChoiceBlock()), ('width', wagtail.core.blocks.IntegerBlock(blank=True, default=None, help_text='optional width in px. Default is auto.', null=True, required=False))], icon='image', label='Aligned image')), ('pullquote', wagtail.core.blocks.StructBlock([('quote', wagtail.core.blocks.TextBlock('quote title')), ('attribution', wagtail.core.blocks.CharBlock())])), ('aligned_html', wagtail.core.blocks.StructBlock([('html', wagtail.core.blocks.RawHTMLBlock()), ('alignment', home.models.HTMLAlignmentChoiceBlock())], icon='code', label='Raw HTML')), ('document', wagtail.documents.blocks.DocumentChooserBlock(icon='doc-full-inverse')), ('wgo', wagtail.core.blocks.StructBlock([('sgf', wagtail.documents.blocks.DocumentChooserBlock()), ('alignment', home.models.WgoAlignmentChoiceBlock()), ('width', wagtail.core.blocks.IntegerBlock(default=700))], label='wgo')), ('table', wagtail.contrib.table_block.blocks.TableBlock()), ('poll', wagtail.snippets.blocks.SnippetChooserBlock(machina.apps.forum_conversation.forum_polls.models.TopicPoll, template='home/includes/poll.html')), ('sponsor', wagtail.core.blocks.StructBlock([]))], blank=True),
        ),
        migrations.AlterField(
            model_name='leftsidebarpage',
            name='body',
            field=wagtail.core.fields.StreamField([('h2', wagtail.core.blocks.CharBlock(form_classname='title', icon='title')), ('h3', wagtail.core.blocks.CharBlock(form_classname='title', icon='title')), ('h4', wagtail.core.blocks.CharBlock(form_classname='title', icon='title')), ('intro', wagtail.core.blocks.RichTextBlock(icon='pilcrow')), ('paragraph', wagtail.core.blocks.RichTextBlock(icon='pilcrow')), ('aligned_image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('caption', wagtail.core.blocks.RichTextBlock(blank=True, null=True, required=False)), ('alignment', home.models.ImageFormatChoiceBlock()), ('width', wagtail.core.blocks.IntegerBlock(blank=True, default=None, help_text='optional width in px. Default is auto.', null=True, required=False))], icon='image', label='Aligned image')), ('pullquote', wagtail.core.blocks.StructBlock([('quote', wagtail.core.blocks.TextBlock('quote title')), ('attribution', wagtail.core.blocks.CharBlock())])), ('aligned_html', wagtail.core.blocks.StructBlock([('html', wagtail.core.blocks.RawHTMLBlock()), ('alignment', home.models.HTMLAlignmentChoiceBlock())], icon='code', label='Raw HTML')), ('document', wagtail.documents.blocks.DocumentChooserBlock(icon='doc-full-inverse')), ('wgo', wagtail.core.blocks.StructBlock([('sgf', wagtail.documents.blocks.DocumentChooserBlock()), ('alignment', home.models.WgoAlignmentChoiceBlock()), ('width', wagtail.core.blocks.IntegerBlock(default=700))], label='wgo')), ('table', wagtail.contrib.table_block.blocks.TableBlock()), ('poll', wagtail.snippets.blocks.SnippetChooserBlock(machina.apps.forum_conversation.forum_polls.models.TopicPoll, template='home/includes/poll.html')), ('sponsor', wagtail.core.blocks.StructBlock([]))], blank=True),
        ),
        migrations.AlterField(
            model_name='rightsidebarpage',
            name='body',
            field=wagtail.core.fields.StreamField([('h2', wagtail.core.blocks.CharBlock(form_classname='title', icon='title')), ('h3', wagtail.core.blocks.CharBlock(form_classname='title', icon='title')), ('h4', wagtail.core.blocks.CharBlock(form_classname='title', icon='title')), ('intro', wagtail.core.blocks.RichTextBlock(icon='pilcrow')), ('paragraph', wagtail.core.blocks.RichTextBlock(icon='pilcrow')), ('aligned_image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('caption', wagtail.core.blocks.RichTextBlock(blank=True, null=True, required=False)), ('alignment', home.models.ImageFormatChoiceBlock()), ('width', wagtail.core.blocks.IntegerBlock(blank=True, default=None, help_text='optional width in px. Default is auto.', null=True, required=False))], icon='image', label='Aligned image')), ('pullquote', wagtail.core.blocks.StructBlock([('quote', wagtail.core.blocks.TextBlock('quote title')), ('attribution', wagtail.core.blocks.CharBlock())])), ('aligned_html', wagtail.core.blocks.StructBlock([('html', wagtail.core.blocks.RawHTMLBlock()), ('alignment', home.models.HTMLAlignmentChoiceBlock())], icon='code', label='Raw HTML')), ('document', wagtail.documents.blocks.DocumentChooserBlock(icon='doc-full-inverse')), ('wgo', wagtail.core.blocks.StructBlock([('sgf', wagtail.documents.blocks.DocumentChooserBlock()), ('alignment', home.models.WgoAlignmentChoiceBlock()), ('width', wagtail.core.blocks.IntegerBlock(default=700))], label='wgo')), ('table', wagtail.contrib.table_block.blocks.TableBlock()), ('poll', wagtail.snippets.blocks.SnippetChooserBlock(machina.apps.forum_conversation.forum_polls.models.TopicPoll, template='home/includes/poll.html')), ('sponsor', wagtail.core.blocks.StructBlock([]))], blank=True),
        ),
        migrations.AlterField(
            model_name='streamfieldentrypage',
            name='streamfield',
            field=wagtail.core.fields.StreamField([('h2', wagtail.core.blocks.CharBlock(form_classname='title', icon='title')), ('h3', wagtail.core.blocks.CharBlock(form_classname='title', icon='title')), ('h4', wagtail.core.blocks.CharBlock(form_classname='title', icon='title')), ('intro', wagtail.core.blocks.RichTextBlock(icon='pilcrow')), ('paragraph', wagtail.core.blocks.RichTextBlock(icon='pilcrow')), ('aligned_image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('caption', wagtail.core.blocks.RichTextBlock(blank=True, null=True, required=False)), ('alignment', home.models.ImageFormatChoiceBlock()), ('width', wagtail.core.blocks.IntegerBlock(blank=True, default=None, help_text='optional width in px. Default is auto.', null=True, required=False))], icon='image', label='Aligned image')), ('pullquote', wagtail.core.blocks.StructBlock([('quote', wagtail.core.blocks.TextBlock('quote title')), ('attribution', wagtail.core.blocks.CharBlock())])), ('aligned_html', wagtail.core.blocks.StructBlock([('html', wagtail.core.blocks.RawHTMLBlock()), ('alignment', home.models.HTMLAlignmentChoiceBlock())], icon='code', label='Raw HTML')), ('document', wagtail.documents.blocks.DocumentChooserBlock(icon='doc-full-inverse')), ('wgo', wagtail.core.blocks.StructBlock([('sgf', wagtail.documents.blocks.DocumentChooserBlock()), ('alignment', home.models.WgoAlignmentChoiceBlock()), ('width', wagtail.core.blocks.IntegerBlock(default=700))], label='wgo')), ('table', wagtail.contrib.table_block.blocks.TableBlock()), ('poll', wagtail.snippets.blocks.SnippetChooserBlock(machina.apps.forum_conversation.forum_polls.models.TopicPoll, template='home/includes/poll.html')), ('sponsor', wagtail.core.blocks.StructBlock([]))], blank=True),
        ),
    ]
