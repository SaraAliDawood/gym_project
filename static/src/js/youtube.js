/** @odoo-module **/

import {registry} from '@web/core/registry';
import { Component } from '@odoo/owl';

class Youtube extends Component {
    setup() {
       
    }
}


Youtube.template = 'gym_project.Youtube';
registry.category('actions').add('gym_project.youtube_action', Youtube);