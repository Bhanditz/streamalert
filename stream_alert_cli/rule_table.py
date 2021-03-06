"""
Copyright 2017-present, Airbnb Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
from stream_alert.shared.rule_table import RuleTable


def rule_staging_handler(options, config):
    """Handle operations related to the rule table (listing, updating, etc)

    Args:
        options (argparse.Namespace): Various options needed by subcommand
            handlers
        config (CLIConfig): Loaded configuration from 'conf/' directory

    Returns:
        bool: False if errors occurred, True otherwise
    """
    if options.subcommand == 'enable':
        config.toggle_rule_staging(options.enable)

    table_name = '{}_streamalert_rules'.format(config['global']['account']['prefix'])
    if options.subcommand == 'status':
        print RuleTable(table_name).__str__(options.verbose)

    if options.subcommand in {'stage', 'unstage'}:
        stage = (options.subcommand == 'stage')
        table = RuleTable(table_name)
        for rule in options.rules:
            table.toggle_staged_state(rule, stage)

    return True
