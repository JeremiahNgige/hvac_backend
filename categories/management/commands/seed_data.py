from django.core.management.base import BaseCommand
from categories.models import Category
from guides.models import Guide, GuideStep
from tips.models import Tip


class Command(BaseCommand):
    help = 'Seed the database with HVAC demo data'

    def handle(self, *args, **options):
        self.stdout.write('Seeding HVAC data...')

        # ---------- Categories ----------
        categories_data = [
            {'name': 'Furnace', 'description': 'Gas and electric furnace maintenance, troubleshooting, and repair guides.', 'icon_name': 'local_fire_department', 'color_hex': '#E65100'},
            {'name': 'Air Conditioner', 'description': 'Central AC unit maintenance, cleaning, and common repair guides.', 'icon_name': 'ac_unit', 'color_hex': '#0277BD'},
            {'name': 'Heat Pump', 'description': 'Heat pump system troubleshooting, seasonal maintenance, and efficiency tips.', 'icon_name': 'heat_pump', 'color_hex': '#00695C'},
            {'name': 'Thermostat', 'description': 'Thermostat installation, programming, and smart thermostat setup guides.', 'icon_name': 'thermostat', 'color_hex': '#4527A0'},
            {'name': 'Ductwork', 'description': 'Air duct inspection, sealing, cleaning, and insulation guides.', 'icon_name': 'air', 'color_hex': '#37474F'},
            {'name': 'Ventilation', 'description': 'Ventilation system maintenance, air quality improvement, and fan repairs.', 'icon_name': 'toys', 'color_hex': '#1B5E20'},
        ]

        cats = {}
        for data in categories_data:
            cat, _ = Category.objects.get_or_create(name=data['name'], defaults=data)
            cats[cat.name] = cat
        self.stdout.write(f'  Created {len(cats)} categories')

        # ---------- Guides ----------
        guides_data = [
            {
                'cat_name': 'Furnace', 'title': 'How to Replace Your Furnace Air Filter',
                'summary': 'Learn how to locate, remove, and replace your furnace air filter to maintain proper airflow and indoor air quality.',
                'difficulty': 'easy', 'estimated_time': '15 minutes', 'is_featured': True,
                'steps': [
                    ('Turn Off the Furnace', 'Switch your furnace to the OFF position or turn off the power at the circuit breaker.', 'Wait 30 seconds after turning off to let any residual airflow stop.'),
                    ('Locate the Filter Compartment', 'Find the filter slot between the return air duct and the blower compartment.', 'Take a photo of the current filter orientation before removing it.'),
                    ('Remove the Old Filter', 'Carefully slide the old filter out. Note the size printed on the frame (e.g., 16x25x1) and the airflow arrow.', ''),
                    ('Insert the New Filter', 'Slide the new filter in with the airflow arrow pointing toward the blower. Ensure a snug fit.', 'Write the installation date on the filter frame with a marker.'),
                    ('Restore Power and Test', 'Turn the furnace back on and set the thermostat to call for heat. Verify air flows through the vents.', 'Set a reminder to check your filter every 30 days.'),
                ],
            },
            {
                'cat_name': 'Furnace', 'title': 'Troubleshooting a Furnace That Won\'t Ignite',
                'summary': 'Step-by-step diagnosis when your gas furnace fails to light, from thermostat checks to igniter inspection.',
                'difficulty': 'medium', 'estimated_time': '30-45 minutes', 'is_featured': True,
                'steps': [
                    ('Check the Thermostat', 'Ensure the thermostat is set to HEAT mode and the set temperature is above the current room temperature.', 'Bump the temperature up 5 degrees above room temp to force the call.'),
                    ('Verify the Gas Supply', 'Check that the gas valve near the furnace is ON (handle parallel to the pipe).', 'If you smell gas strongly, leave immediately and call your gas company.'),
                    ('Inspect the Air Filter', 'A severely clogged filter can cause overheating and shutdown. Replace if dirty.', ''),
                    ('Check the Igniter', 'Open the access panel and inspect the hot surface igniter for visible cracks or breaks.', 'Handle the igniter carefully — the ceramic element is very fragile.'),
                    ('Reset the Furnace', 'Turn off the power for 30 seconds, then turn it back on to reset the control board.', 'Note any blinking LED codes on the control board — they indicate specific errors.'),
                    ('Check the Flame Sensor', 'If the furnace ignites but shuts off quickly, clean the flame sensor with fine sandpaper.', 'A dirty flame sensor is one of the most common and cheapest furnace fixes.'),
                ],
            },
            {
                'cat_name': 'Air Conditioner', 'title': 'Cleaning Your AC Condenser Coils',
                'summary': 'Improve your AC efficiency by cleaning outdoor condenser coils — a simple maintenance task that saves energy.',
                'difficulty': 'easy', 'estimated_time': '45 minutes', 'is_featured': True,
                'steps': [
                    ('Turn Off the AC Unit', 'Switch off at thermostat and disconnect switch near the outdoor unit.', ''),
                    ('Remove Debris', 'Clear leaves, grass clippings, and debris. Maintain at least 2 feet of clearance.', 'Trim back bushes or plants that have grown too close.'),
                    ('Remove the Fan Guard', 'Unscrew the top fan guard/grille. Lift the fan assembly out carefully.', ''),
                    ('Clean the Coil Fins', 'Spray fins from inside out with a garden hose (NOT a pressure washer). Use coil cleaner for stubborn buildup.', 'Always spray from inside out to push dirt outward.'),
                    ('Straighten Bent Fins', 'Use a fin comb or butter knife to gently straighten bent aluminum fins.', 'Be gentle — the fins are thin and can break easily.'),
                    ('Reassemble and Test', 'Replace the fan guard, restore power, and set thermostat to cool.', 'Do this at the start of every cooling season.'),
                ],
            },
            {
                'cat_name': 'Air Conditioner', 'title': 'How to Unclog an AC Condensate Drain Line',
                'summary': 'A clogged drain line can cause water damage. Learn to clear blockages with simple tools.',
                'difficulty': 'easy', 'estimated_time': '20 minutes', 'is_featured': False,
                'steps': [
                    ('Turn Off the AC', 'Turn off at the thermostat and breaker.', ''),
                    ('Locate the Drain Line', 'Find the PVC condensate drain line near the indoor air handler.', 'Place towels around the drain pan if there is standing water.'),
                    ('Clear with Vinegar', 'Pour 1 cup distilled white vinegar into the drain access point. Let sit 30 minutes.', 'For stubborn clogs, use a wet/dry vacuum on the outdoor end.'),
                    ('Flush with Water', 'Flush the line with warm water. Check the outdoor exit for free flow.', 'Pour vinegar monthly during cooling season to prevent clogs.'),
                ],
            },
            {
                'cat_name': 'Thermostat', 'title': 'Installing a Smart Thermostat',
                'summary': 'Replace your old thermostat with a smart one for better comfort and energy savings.',
                'difficulty': 'medium', 'estimated_time': '30-45 minutes', 'is_featured': True,
                'steps': [
                    ('Check Compatibility', 'Verify your system is compatible. Most smart thermostats require a C-wire.', 'Use online compatibility checkers. Photo your current wiring first.'),
                    ('Turn Off HVAC Power', 'Turn off power at the circuit breaker.', ''),
                    ('Remove the Old Thermostat', 'Remove faceplate and label each wire with its terminal letter (R, W, Y, G, C).', 'Wrap tape around each wire and write the terminal letter on it.'),
                    ('Install the New Base Plate', 'Mount the new base plate using a level. Mark and drill screw holes.', 'Measure if the new plate covers the old mounting mark.'),
                    ('Connect the Wires', 'Connect each labeled wire to its corresponding terminal.', 'If no C-wire, some thermostats include a power extender kit.'),
                    ('Configure', 'Snap on the display, restore power, and follow the setup wizard for WiFi and scheduling.', 'Enable learning/adaptive features for automatic optimization.'),
                ],
            },
            {
                'cat_name': 'Heat Pump', 'title': 'Seasonal Heat Pump Maintenance Checklist',
                'summary': 'Keep your heat pump efficient year-round with this seasonal maintenance routine.',
                'difficulty': 'easy', 'estimated_time': '1 hour', 'is_featured': True,
                'steps': [
                    ('Replace the Air Filter', 'Check monthly, replace every 1-3 months.', 'Buy filters in bulk to always have replacements.'),
                    ('Clean the Outdoor Unit', 'Remove debris and hose down coil fins. Maintain 2 feet of clearance.', 'In winter, gently remove ice — let the defrost cycle handle most of it.'),
                    ('Check Refrigerant Lines', 'Inspect insulation on lines between indoor and outdoor units. Replace if damaged.', 'Black foam insulation tape is inexpensive and easy to apply.'),
                    ('Clean Indoor Coil and Drain', 'Clean the evaporator coil with a soft brush. Flush the condensate drain with vinegar.', ''),
                    ('Test Both Modes', 'Test heating and cooling modes during seasonal changeover.', 'Listen for unusual sounds indicating failing components.'),
                ],
            },
            {
                'cat_name': 'Ductwork', 'title': 'How to Seal Leaky Air Ducts',
                'summary': 'Leaky ducts waste 20-30% of conditioned air. Find and seal leaks to improve comfort and save energy.',
                'difficulty': 'medium', 'estimated_time': '2-3 hours', 'is_featured': False,
                'steps': [
                    ('Identify Leaks', 'Turn on the fan and feel for air escaping at joints. Use tissue to detect fluttering.', 'Focus on ducts closest to the air handler where pressure is highest.'),
                    ('Gather Materials', 'Get mastic sealant or metal-backed UL 181 tape. Avoid standard duct tape.', 'Mastic is the best long-term solution — apply with a paintbrush.'),
                    ('Clean Surfaces', 'Wipe the area around each leak with a damp cloth for proper adhesion.', ''),
                    ('Apply Sealant', 'Apply mastic generously over joints, extending 1 inch beyond seams. Use mesh tape for larger gaps.', 'Let mastic dry 24 hours before running the system.'),
                    ('Insulate Ducts', 'Wrap ducts in unconditioned spaces with R-6 or R-8 insulation.', 'Insulating attic ducts can reduce energy loss by 10-15%.'),
                ],
            },
            {
                'cat_name': 'Ventilation', 'title': 'Cleaning Bathroom Exhaust Fans',
                'summary': 'A dirty exhaust fan can\'t remove moisture properly, leading to mold. Clean it in a few simple steps.',
                'difficulty': 'easy', 'estimated_time': '20 minutes', 'is_featured': False,
                'steps': [
                    ('Turn Off the Fan', 'Switch off at the wall switch. For safety, turn off the circuit breaker too.', ''),
                    ('Remove the Cover', 'Pull the cover down and squeeze spring clips to release. Some models use screws.', 'Place a towel below to catch falling dust.'),
                    ('Clean Cover and Blades', 'Wash the cover in warm soapy water. Vacuum dust from fan blades and motor housing.', 'Compressed air works great for hard-to-reach motor dust.'),
                    ('Reinstall and Test', 'Reattach the cover, restore power, and test — the fan should spin freely and quietly.', 'Clean exhaust fans every 6 months for optimal performance.'),
                ],
            },
        ]

        guide_count = 0
        for gdata in guides_data:
            cat_name = gdata.pop('cat_name')
            steps_data = gdata.pop('steps')
            guide, created = Guide.objects.get_or_create(
                title=gdata['title'],
                defaults={**gdata, 'category': cats[cat_name]}
            )
            if created:
                for i, (title, desc, pro_tip) in enumerate(steps_data, 1):
                    GuideStep.objects.create(
                        guide=guide, step_number=i,
                        title=title, description=desc, pro_tip=pro_tip
                    )
                guide_count += 1
        self.stdout.write(f'  Created {guide_count} guides')

        # ---------- Tips ----------
        tips_data = [
            {'title': 'Always Turn Off Power First', 'content': 'Before any HVAC maintenance, turn off power at the thermostat AND circuit breaker to prevent shock and equipment damage.', 'tip_type': 'safety', 'is_featured': True},
            {'title': 'Gas Leak Safety Protocol', 'content': 'If you smell rotten eggs near your furnace, do NOT flip switches. Leave immediately and call your gas company from outside.', 'tip_type': 'safety', 'is_featured': True},
            {'title': 'Change Filters Regularly', 'content': 'Replace HVAC air filters every 30-90 days. Clean filters improve airflow, reduce energy use by 5-15%, and extend equipment life.', 'tip_type': 'maintenance', 'is_featured': True},
            {'title': 'Schedule Professional Maintenance', 'content': 'Schedule professional HVAC inspection yearly — spring for cooling, fall for heating. Pros catch issues DIY maintenance may miss.', 'tip_type': 'maintenance', 'is_featured': True},
            {'title': 'Seal and Insulate Ducts', 'content': 'Leaky ducts reduce efficiency by 20-30%. Use mastic sealant or metal-backed tape to seal joints, and insulate ducts in unconditioned spaces.', 'tip_type': 'energy', 'is_featured': True},
            {'title': 'Use a Programmable Thermostat', 'content': 'Setting the thermostat back 7-10°F for 8 hours daily saves up to 10% yearly on heating and cooling costs.', 'tip_type': 'energy', 'is_featured': True},
            {'title': 'Keep Vents Clear', 'content': 'Ensure furniture, curtains, and rugs don\'t block supply or return vents. Blocked vents create pressure imbalances and reduce efficiency.', 'tip_type': 'maintenance', 'is_featured': False},
            {'title': 'Know When to Call a Pro', 'content': 'Some tasks require a licensed technician: refrigerant handling, electrical modifications, gas line work, and any repair you\'re unsure about.', 'tip_type': 'safety', 'is_featured': False},
            {'title': 'Keep Outdoor Units Clear', 'content': 'Maintain 2+ feet of clearance around outdoor AC/heat pump units. Trim vegetation, remove debris, and don\'t stack items nearby.', 'tip_type': 'maintenance', 'is_featured': False},
            {'title': 'Use Ceiling Fans to Supplement', 'content': 'Ceiling fans make rooms feel 4-6°F cooler. Run counter-clockwise in summer, clockwise on low in winter to redistribute warm air.', 'tip_type': 'energy', 'is_featured': False},
        ]

        tip_count = 0
        for tdata in tips_data:
            _, created = Tip.objects.get_or_create(title=tdata['title'], defaults=tdata)
            if created:
                tip_count += 1
        self.stdout.write(f'  Created {tip_count} tips')
        self.stdout.write(self.style.SUCCESS('Seeding complete!'))
