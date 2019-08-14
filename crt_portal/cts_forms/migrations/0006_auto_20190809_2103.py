# Generated by Django 2.2.3 on 2019-08-09 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cts_forms', '0005_delete_choice'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('primary_complaint', models.CharField(choices=[('fired', 'Fired, not hired, demoted, or asked to show more documentation than required'), ('denied_access', 'Denied access or removed from a location (including segregation)'), ('harassed', 'Harassed, threatened, assaulted, or otherwise made to feel unsafe (including sexual harassment or assault)'), ('retaliated', 'Retaliated against or otherwise mistreated for reporting an issue'), ('prevented_from_service', 'Prevented from using a service or service terminated'), ('denied_housing', 'Denied housing or subjected to harmful living conditions'), ('vote', 'Ability to vote was impacted'), ('discriminated_against', 'Otherwise discriminated against')], max_length=100)),
                ('protected_class', models.CharField(blank=True, choices=[('age', 'Age'), ('familial_status', 'Familial, marital, or parental status'), ('sexual_orientation', 'Sexual orientation'), ('military_status', 'Military status'), ('disability', 'Disability (including temporary)'), ('national_origin', 'National origin (including ancestry, ethnicity, and language)'), ('sex_gender', 'Sex or gender identity (including pregnancy)'), ('genetic_information', 'Genetic information'), ('race_color', 'Race/color'), ('immigration_citizenship', 'Immigration/citizenship status (you do not have to divulge your status)'), ('religion', 'Religion')], max_length=100, null=True)),
                ('place', models.CharField(blank=True, choices=[('store', 'Retail/commercial building (store, restaurant, hotel, nightclub, theater, gym, or other commercial space)'), ('place_of_worship', 'Place of worship'), ('healthcare', 'Healthcare facility (including mental health or long-term care)'), ('incarcerated', 'Prison, jail, or juvenile corrections facility, or while otherwise incarcerated'), ('school', 'Educational institution (school, university), education program or educational activity (after school program or workshop)'), ('public_space', 'Outdoor public space (including car, street, sidewalk, park)'), ('voting', 'Voting location or ballot (including mail-in ballots)'), ('workplace', 'Workplace or potential workplace'), ('home,', 'Home, potential home, or services to help with purchasing a home (banks, lenders, or other financial services)'), ('government_building', 'Another government building (courthouse, DMV, post office)')], max_length=100, null=True)),
                ('public_or_private_employer', models.CharField(blank=True, choices=[('private_employer', 'Private employer -- Businesses or non-profits not funded by the government such as retail stores, banks, or restaurants.'), ('public_employer', 'Public employer -- Funded by the government like a post office, fire department, courthouse, DMV, or public school. This could be at the local, state, or federal level.'), ('not_sure', "I'm not sure")], max_length=100, null=True)),
                ('employer_size', models.CharField(blank=True, choices=[('14_or_less', 'Fewer than 15 employees'), ('15_or_more', '15 or more employees')], max_length=100, null=True)),
                ('public_or_private_school', models.CharField(blank=True, choices=[('not_sure', "I'm not sure"), ('private', 'Private -- Schools or programs funded privately such as charter schools, magnet schools, or faith-based colleges'), ('public', 'Public -- Schools or programs funded by local, state, or the federal government')], max_length=100, null=True)),
                ('public_or_private_facility', models.CharField(blank=True, choices=[('private_facility', 'Private facility'), ('federal_facility', 'Federal facility'), ('state_local_facility', 'State or local facility'), ('not_sure', 'Not sure')], max_length=100, null=True)),
                ('public_or_private_healthcare', models.CharField(blank=True, choices=[('private_facility', 'Private facility'), ('federal_facility', 'Federal facility'), ('state_local_facility', 'State or local facility'), ('not_sure', 'Not sure')], max_length=100, null=True)),
                ('respondent_type', models.CharField(blank=True, choices=[('employer', 'Employer or potential employer'), ('healthcare', 'Healthcare provider or staff'), ('landlord', 'Landlord, leasing office, or home/rental provider'), ('other_public_official', 'Other public official (judge, voting official, or other government official)'), ('lender', 'Bank or loaning service'), ('school', 'Individual(s) from school or educational program (teacher, administrator, staff, or students)'), ('police_corrections_staff', 'Police, prison guard, or other corrections staff')], max_length=100, null=True)),
                ('respondent_contact_ask', models.BooleanField(null=True)),
                ('respondent_name', models.CharField(blank=True, max_length=700, null=True)),
                ('respondent_city', models.CharField(blank=True, max_length=700, null=True)),
                ('violation_summary', models.TextField()),
                ('when', models.CharField(blank=True, choices=[('greater_than_3_years', 'More than 3 years ago'), ('last_3_years', 'Within the last 3 years'), ('last_6_months', 'Within the last 6 months')], max_length=700, null=True)),
                ('how_many', models.CharField(blank=True, choices=[('yes', 'Yes'), ('not_sure', "I'm not sure"), ('no', 'No')], max_length=700, null=True)),
                ('who_reporting_for', models.CharField(blank=True, choices=[('employer', 'Employer or potential employer'), ('healthcare', 'Healthcare provider or staff'), ('landlord', 'Landlord, leasing office, or home/rental provider'), ('Individual(s) from school or educational program (teacher, administrator, staff, or students)', 'Individual(s) from school or educational program (teacher, administrator, staff, or students)'), ('other_public_official', 'Other public official (judge, voting official, or other government official)'), ('lender', 'Bank or loaning service'), ('police_corrections_staff', 'Police, prison guard, or other corrections staff')], max_length=100, null=True)),
                ('relationship', models.CharField(blank=True, choices=[('myself', "I'm reporting for myself"), ('another', "I'm reporting on behalf of another person"), ('undisclosed', 'I prefer not to disclose')], max_length=100, null=True)),
                ('do_not_contact', models.BooleanField(null=True)),
                ('contact_given_name', models.CharField(blank=True, max_length=800, null=True)),
                ('contact_family_name', models.CharField(blank=True, max_length=800, null=True)),
                ('contact_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('contact_address_line_1', models.CharField(blank=True, max_length=700, null=True)),
                ('contact_address_line_2', models.CharField(blank=True, max_length=700, null=True)),
                ('contact_phone', models.CharField(blank=True, max_length=200, null=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('contact_state', models.ManyToManyField(blank=True, related_name='contact_state', to='cts_forms.State')),
                ('respondent_state', models.ManyToManyField(blank=True, related_name='respondent_state', to='cts_forms.State')),
            ],
        ),
        migrations.DeleteModel(
            name='ViolationReport',
        ),
    ]
