#!/usr/bin/env python

#
# copyright Tom Goetz
#

import collections

from Data import *
from Field import *
from MessageType import MessageType


class DefinitionMessageData(object):

    known_messages = {
        MessageType.file_id : {
            0: FileField('type'),
            1 : ManufacturerField(),
            2 : ProductField(),
            3 : Field('serial_number'),
            4 : TimestampField('time_created'),
            5 : Field('number'),
            7 : StringField('product_name')
        },
        MessageType.capabilities : {},
        MessageType.device_settings : {
            0 : Field('active_time_zone'),
            1 : Field('utc_offset'),
            2 : Field('time_offset'),
            4 : TimeModeField(),
            5 : Field('time_zone_offset'),
            12 : BacklightModeField(),
            35 : SwitchField('switch_35'),
            36 : BoolField('activity_tracker_enabled'),
            38 : SwitchField('switch_38'),
            39 : TimestampField('clock_time'),
            40 : Field('pages_enabled'),
            41 : SwitchField('switch_41'),
            42 : SwitchField('switch_42'),
            43 : SwitchField('switch_43'),
            44 : SwitchField('switch_44'),
            45 : SwitchField('switch_45'),
            46 : BoolField('move_alert_enabled'),
            47 : DateModeField(),
            48 : SwitchField('switch_48'),
            49 : SwitchField('switch_49'),
            52 : SwitchField('switch_52'),
            53 : SwitchField('switch_53'),
            55 : DisplayOrientationField('display_orientation'),
            56 : SideField(),
            57 : Field('default_page'),
            58 : Field('autosync_min_steps'),
            59 : Field('autosync_min_time'),
            64 : SwitchField('switch_64'),
            65 : SwitchField('switch_65'),
            68 : SwitchField('switch_68'),
            80 : BoolField('lactate_threshold_autodetect_enabled'),
            81 : SwitchField('switch_81'),
            82 : SwitchField('switch_82'),
            83 : SwitchField('switch_83'),
            84 : SwitchField('switch_84'),
            85 : SwitchField('switch_85'),
            86 : BoolField('ble_auto_upload_enabled'),
            87 : SwitchField('switch_87'),
            89 : AutoSyncFrequencyField(),
            90 : AutoActivityDetectField(),
            94 : Field('number_of_screens'),
            95 : DisplayOrientationField('smart_notification_display_orientation'),
            107 : SwitchField('switch_107'),
            108 : SwitchField('switch_108'),
            109 : SwitchField('switch_109'),
            110 : SwitchField('switch_110'),
            111 : SwitchField('switch_111'),
            112 : SwitchField('switch_112'),
            126 : SwitchField('switch_126'),
            127 : SwitchField('switch_127'),
            128 : SwitchField('switch_128'),
            133 : SwitchField('switch_133'),
            134 : SwitchField('tap_interface'),
            141 : SwitchField('switch_141'),
        },
        MessageType.user_profile : {
            1 : GenderField(),
            2 : Field('age'),
            3 : HeightField(),
            4 : WeightField(),
            5 : LanguageField(),
            6 : DisplayMeasureField('elev_setting'),
            7 : DisplayMeasureField('weight_setting'),
            8 : HeartRateField('resting_heart_rate'),
            9 : HeartRateField('default_max_running_heart_rate'),
            10 : HeartRateField('default_max_biking_heart_rate'),
            11 : HeartRateField('default_max_heart_rate'),
            12 : DisplayHeartField('hr_setting'),
            13 : DisplayMeasureField('speed_setting'),
            14 : DisplayMeasureField('dist_setting'),
            16 : PowerField('power_setting'),
            17 : ActivityClassField('activity_class'),
            18 : DisplayPositionField('position_setting'),
            21 : DisplayMeasureField('temperature_setting'),
            22 : Field('local_id'),
            23 : Field('global_id'),
            28 : TimeOfDayField('wake_time'),
            29 : TimeOfDayField('sleep_time'),
            30 : DisplayMeasureField('height_setting'),
            31 : EnhancedDistanceMetersField('user_running_step_length'),
            32 : EnhancedDistanceMetersField('user_walking_step_length'),
            35 : TimestampField('ts_35'),
            41 : TimestampField('ts_41'),
            47 : DisplayMeasureField('depth_setting'),
            49 : Field('dive_count'),
        },
        MessageType.hrm_profile : {
            0 : BoolField('enabled'),
            1 : Field('hrm_ant_id'),
            2 : BoolField('log_hrv'),
            3 : Field('hrm_ant_id_trans_type'),
        },
        MessageType.sdm_profile : {},
        MessageType.bike_profile : {
            0 : StringField('name'),
            1 : SportField(),
            2 : SubSportField(),
            3 : DistanceCentimetersToMetersField('odometer'),
            4 : Field('bike_spd_ant_id'),
            5 : Field('bike_cad_ant_id'),
            6 : Field('bike_spdcad_ant_id'),
            7 : Field('bike_power_ant_id'),
            8 : DistanceMillimetersToMetersField('custom_wheelsize'),
            9 : DistanceMillimetersToMetersField('auto_wheelsize'),
            10 : WeightField('bike_weight'),
            11 : PercentField('power_cal_factor'),
            12 : BoolField('auto_wheel_cal'),
            13 : BoolField('auto_power_zero'),
            14 : Field('id'),
            15 : BoolField('spd_enabled'),
            16 : BoolField('cad_enabled'),
            17 : BoolField('spdcad_enabled'),
            18 : BoolField('power_enabled'),
            19 : DistanceMillimetersToMetersField('crank_length'),
            20 : BoolField('enabled'),
            21 : Field('bike_spd_ant_id_trans_type'),
            22 : Field('bike_cad_ant_id_trans_type'),
            23 : Field('bike_spdcad_ant_id_trans_type'),
            24 : Field('bike_power_ant_id_trans_type'),
            37 : Field('odometer_rollover'),
        },
        MessageType.zones_target : {
            1 : Field('max_heart_rate'),
            2 : Field('threshold_heart_rate'),
            3 : Field('functional_threshold_power'),
            5 : HeartRateZoneCalcField(),
            7 : PowerCalcField()
        },
        MessageType.hr_zone : {
            1 : HeartRateField('high_bpm'),
            2 : StringField('name'),
        },
        MessageType.power_zone : {
            1 : PowerField('high_value'),
            2 : StringField('name'),
        },
        MessageType.met_zone : {},
        MessageType.sport : {
            0 : SportField(),
            1 : SubSportField(),
            3 : StringField('name'),
        },
        MessageType.unknown_13 : {
            5 : PosField('position_5'),
            6 : PosField('position_6'),
        },
        MessageType.goal : {
            0 : SportField(),
            1 : SubSportField(),
            2 : TimestampField('start_time'),
            3 : TimestampField('end_time'),
            4 : GoalTypeField('type'),
            5 : Field('value'),
            6 : BoolField('repeat'),
            7 : GoalValueField(),
            8 : GoalRecurrenceField('recurrence'),
            9 : Field('recurrence_value'),
            10 : BoolField('enabled'),
            11 : GoalSourceField('source')
        },
        MessageType.session : {
            0 : EventField(),
            1 : EventTypeField(),
            2 : TimestampField('start_time'),
            3 : LatiitudeField('start_position_lat'),
            4 : LongitudeField('start_position_long'),
            5 : SportField(),
            6 : SubSportField(),
            7 : TimeMsField('total_elapsed_time'),
            8 : TimeMsField('total_timer_time'),
            9 : DistanceCentimetersToKmsField('total_distance'),
            10 : SportBasedCyclesField('total_cycles'),
            11 : CaloriesField('total_calories'),
            13 : CaloriesField('total_fat_calories'),
            14 : SpeedMpsField('avg_speed'),
            15 : SpeedMpsField('max_speed'),
            16 : HeartRateField('avg_heart_rate'),
            17 : HeartRateField('max_heart_rate'),
            18 : CadenceField('avg_cadence'),
            19 : CadenceField('max_cadence'),
            20 : PowerField('avg_power'),
            21 : PowerField('max_power'),
            22 : DistanceMetersField('total_ascent'),
            23 : DistanceMetersField('total_descent'),
            24 : TrainingeffectField('total_training_effect'),
            25 : Field('first_lap_index'),
            26 : Field('num_laps'),
            27 : Field('event_group'),
            28 : SessionTriggerField(),
            29 : LatiitudeField('nec_lat'),
            30 : LongitudeField('nec_long'),
            31 : LatiitudeField('swc_lat'),
            32 : LongitudeField('swc_long'),
            33 : Field('length_count'),
            34 : PowerField('normalized_power'),
            35 : TrainingeffectField('training_stress_score'),
            36 : Field('intensity_factor'),
            37 : LeftRightBalanceField('left_right_balance'),
            38 : LatiitudeField('end_position_lat'),
            39 : LongitudeField('end_position_long'),
            41 : Field('avg_stroke_count'),
            42 : DistanceCentimetersToMetersField('avg_stroke_distance'),
            43 : Field('swim_stroke'),
            44 : DistanceMetersField('pool_length'),
            45 : PowerField('threshold_power'),
            46 : DisplayMeasureField('pool_length_unit'),
            47 : Field('num_active_lengths'),
            48 : WorkField('total_work'),
            49 : EnhancedAltitudeField('avg_altitude'),
            50 : EnhancedAltitudeField('max_altitude'),
            51 : DistanceMetersField('gps_accuracy'),
            52 : PercentField('avg_grade'),
            53 : PercentField('avg_pos_grade'),
            54 : PercentField('avg_neg_grade'),
            55 : PercentField('max_pos_grade'),
            56 : PercentField('max_neg_grade'),
            57 : TemperatureField('avg_temperature'),
            58 : TemperatureField('max_temperature'),
            59 : TimeMsField('total_moving_time'),
            60 : SpeedMpsField('avg_pos_vertical_speed'),
            61 : SpeedMpsField('avg_neg_vertical_speed'),
            62 : SpeedMpsField('max_pos_vertical_speed'),
            63 : SpeedMpsField('max_neg_vertical_speed'),
            64 : HeartRateField('min_heart_rate'),
            65 : TimeMsField('time_in_hr_zone'),
            66 : TimeMsField('time_in_speed_zone'),
            67 : TimeMsField('time_in_cadence_zone'),
            68 : TimeMsField('time_in_power_zone'),
            69 : TimeMsField('avg_lap_time'),
            70 : Field('best_lap_index'),
            71 : EnhancedAltitudeField('min_altitude'),
            78 : Field('total_swim_time'),
            79 : Field('average_stroke'),
            80 : Field('swolf'),
            82 : Field('player_score'),
            83 : Field('opponent_score'),
            84 : StringField('opponent_name'),
            85 : Field('stroke_count'),
            86 : Field('zone_count'),
            87 : SpeedMpsField('max_ball_speed'),
            88 : SpeedMpsField('avg_ball_speed'),
            89 : DistanceMillimetersField('avg_vertical_oscillation'),
            90 : PercentField('avg_stance_time_percent'),
            91 : TimeMsField('avg_stance_time', 10.0),
            92 : FractionalCadenceField('avg_fractional_cadence'),
            93 : FractionalCadenceField('max_fractional_cadence'),
            94 : FractionalCyclesField('total_fractional_cycles'),
            95 : Field('avg_total_hemoglobin_conc'),
            96 : Field('min_total_hemoglobin_conc'),
            97 : Field('max_total_hemoglobin_conc'),
            98 : PercentField('avg_saturated_hemoglobin_percent'),
            99 : PercentField('min_saturated_hemoglobin_percent'),
            100 : PercentField('max_saturated_hemoglobin_percent'),
            101 : BytePercentField('avg_left_torque_effectiveness'),
            102 : BytePercentField('avg_right_torque_effectiveness'),
            103 : BytePercentField('avg_left_pedal_smoothness'),
            104 : BytePercentField('avg_right_pedal_smoothness'),
            105 : BytePercentField('avg_combined_pedal_smoothness'),
            110 : StringField('sport_name'),
            111 : Field('sport_index'),
            112 : TimeMsField('time_standing'),
            113 : Field('stand_count'),
            114 : Field('avg_left_pco'),
            115 : Field('avg_right_pco'),
            116 : Field('avg_left_power_phase'),
            117 : Field('avg_left_power_phase_peak'),
            118 : Field('avg_right_power_phase'),
            119 : Field('avg_right_power_phase_peak'),
            120 : PowerField('avg_power_position'),
            121 : PowerField('max_power_position'),
            122 : CadenceField('avg_cadence_position'),
            123 : CadenceField('max_cadence_position'),
            124 : SpeedMpsField('enhanced_avg_speed'),
            125 : SpeedMpsField('enhanced_max_speed'),
            126 : EnhancedAltitudeField('enhanced_avg_altitude'),
            127 : EnhancedAltitudeField('enhanced_min_altitude'),
            128 : EnhancedAltitudeField('enhanced_max_altitude'),
            129 : PowerField('avg_lev_motor_power'),
            130 : PowerField('max_lev_motor_power'),
            131 : BytePercentField('lev_battery_consumption'),
            132 : PercentField('avg_vertical_ratio'),
            133 : PercentField('avg_stance_time_balance'),
            134 : DistanceMillimetersField('avg_step_length'),
            137 : TrainingeffectField('total_anaerobic_training_effect'),
            139 : SpeedMpsField('avg_vam'),
        },
        MessageType.lap : {
            0 : EventField(),
            1 : EventTypeField(),
            2 : TimestampField('start_time'),
            3 : LatiitudeField('start_position_lat'),
            4 : LongitudeField('start_position_long'),
            5 : LatiitudeField('end_position_lat'),
            6 : LongitudeField('end_position_long'),
            7 : TimeMsField('total_elapsed_time'),
            8 : TimeMsField('total_timer_time'),
            9 : DistanceCentimetersToKmsField('total_distance'),
            10 : SportBasedCyclesField('total_cycles'),
            11 : CaloriesField('total_calories'),
            12 : CaloriesField('total_fat_calories'),
            13 : SpeedMpsField('avg_speed'),
            14 : SpeedMpsField('max_speed'),
            15 : Field('avg_heart_rate'),
            16 : Field('max_heart_rate'),
            17 : Field('avg_cadence'),
            18 : Field('max_cadence'),
            19 : Field('avg_power'),
            20 : Field('max_power'),
            21 : DistanceMetersField('total_ascent'),
            22 : DistanceMetersField('total_descent'),
            24 : LapTriggerField(),
            25 : SportField(),
            26 : Field('event_group'),
            27 : PosField('unknown_lat_27'),
            28 : PosField('unknown_long_28'),
            29 : PosField('unknown_lat_29'),
            30 : PosField('unknown_long_30'),
            32 : Field('num_lengths'),
            33 : PowerField('normalized_power'),
            34 : LeftRightBalanceField('left_right_balance'),
            35 : Field('first_length_index'),
            37 : DistanceCentimetersToMetersField('avg_stroke_distance'),
            38 : Field('swim_stroke'),
            39 : SubSportField(),
            40 : Field('num_active_lengths'),
            41 : WorkField('total_work'),
            42 : EnhancedAltitudeField('avg_altitude'),
            43 : EnhancedAltitudeField('max_altitude'),
            44 : DistanceMetersField('gps_accuracy'),
            45 : PercentField('avg_grade'),
            46 : PercentField('avg_pos_grade'),
            47 : PercentField('avg_neg_grade'),
            48 : PercentField('max_pos_grade'),
            49 : PercentField('max_neg_grade'),
            50 : TemperatureField('avg_temperature'),
            51 : TemperatureField('max_temperature'),
            52 : TimeMsField('total_moving_time'),
            53 : SpeedMpsField('avg_pos_vertical_speed'),
            54 : SpeedMpsField('avg_neg_vertical_speed'),
            55 : SpeedMpsField('max_pos_vertical_speed'),
            56 : SpeedMpsField('max_neg_vertical_speed'),
            57 : TimeMsField('time_in_hr_zone'),
            58 : TimeMsField('time_in_speed_zone'),
            59 : TimeMsField('time_in_cadence_zone'),
            60 : TimeMsField('time_in_power_zone'),
            61 : Field('repetition_num'),
            62 : EnhancedAltitudeField('min_altitude'),
            63 : HeartRateField('min_heart_rate'),
            70 : Field('swim_time'),
            71 : MessageIndexField('wkt_step_index'),
            72 : Field('average_stroke'),
            73 : Field('swolf'),
            74 : Field('opponent_score'),
            75 : Field('stroke_count'),
            76 : Field('zone_count'),
            77 : DistanceMillimetersField('avg_vertical_oscillation'),
            78 : PercentField('avg_stance_time_percent'),
            79 : TimeMsField('avg_stance_time', 10.0),
            80 : FractionalCadenceField('avg_fractional_cadence'),
            81 : FractionalCadenceField('max_fractional_cadence'),
            82 : FractionalCyclesField('total_fractional_cycles'),
            83 : Field('player_score'),
            84 : Field('avg_total_hemoglobin_conc'),
            85 : Field('min_total_hemoglobin_conc'),
            86 : Field('max_total_hemoglobin_conc'),
            87 : PercentField('avg_saturated_hemoglobin_percent'),
            88 : PercentField('min_saturated_hemoglobin_percent'),
            89 : PercentField('max_saturated_hemoglobin_percent'),
            91 : BytePercentField('avg_left_torque_effectiveness'),
            92 : BytePercentField('avg_right_torque_effectiveness'),
            93 : BytePercentField('avg_left_pedal_smoothness'),
            94 : BytePercentField('avg_right_pedal_smoothness'),
            95 : BytePercentField('avg_combined_pedal_smoothness'),
            98 : TimeMsField('time_standing'),
            99 : Field('stand_count'),
            100 : Field('avg_left_pco'),
            101 : Field('avg_right_pco'),
            102 : Field('avg_left_power_phase'),
            103 : Field('avg_left_power_phase_peak'),
            104 : Field('avg_right_power_phase'),
            105 : Field('avg_right_power_phase_peak'),
            106 : PowerField('avg_power_position'),
            107 : PowerField('max_power_position'),
            108 : CadenceField('avg_cadence_position'),
            109 : CadenceField('max_cadence_position'),
            110 : SpeedMpsField('enhanced_avg_speed'),
            111 : SpeedMpsField('enhanced_max_speed'),
            112 : EnhancedAltitudeField('enhanced_avg_altitude'),
            113 : EnhancedAltitudeField('enhanced_min_altitude'),
            114 : EnhancedAltitudeField('enhanced_max_altitude'),
            115 : PowerField('avg_lev_motor_power'),
            116 : PowerField('max_lev_motor_power'),
            117 : BytePercentField('lev_battery_consumption'),
            118 : PercentField('avg_vertical_ratio', 100.0),
            119 : PercentField('avg_stance_time_balance'),
            120 : DistanceMillimetersField('avg_step_length'),
            121 : SpeedMpsField('avg_vam'),
        },
        MessageType.record : {
            0 : LatiitudeField('position_lat'),
            1 : LongitudeField('position_long'),
            2 : AltitudeField(),
            3 : HeartRateField('heart_rate'),
            4 : Field('cadence'),
            5 : DistanceCentimetersToKmsField('distance'),
            6 : SpeedMpsField('speed'),
            7 : PowerField(),
            8 : Field('compressed_speed_distance'),
            9 : PercentField('grade'),
            10 : Field('resistance'),
            11 : TimeMsField('time_from_course'),
            12 : DistanceMetersField('cycle_length', 100),
            13 : TemperatureField('temperature'),
            17 : SpeedMpsField('speed_1s'),
            18 : ActivityBasedCyclesField(),
            19 : ActivityBasedCyclesField('total_cycles'),
            28 : Field('compressed_accumulated_power'),
            29 : Field('accumulated_power'),
            30 : LeftRightBalanceField('left_right_balance'),
            31 : DistanceMetersField('gps_accuracy'),
            32 : SpeedMpsField('vertical_speed'),
            33 : CaloriesField('calories'),
            39 : DistanceMillimetersField('avg_vertical_oscillation'),
            40 : PercentField('stance_time_percent'),
            41 : TimeMsField('stance_time', 10.0),
            42 : ActivityTypeField(),
            43 : BytePercentField('left_torque_effectiveness'),
            44 : BytePercentField('right_torque_effectiveness'),
            45 : BytePercentField('left_pedal_smoothness'),
            46 : BytePercentField('right_pedal_smoothness'),
            47 : BytePercentField('combined_pedal_smoothness'),
            48 : Field('time128'),
            49 : Field('stroke_type'),
            50 : Field('zone'),
            51 : Field('ball_speed'),
            52 : Field('cadence256'),
            53 : Field('fractional_cadence'),
            54 : Field('total_hemoglobin_conc'),
            55 : Field('total_hemoglobin_conc_min'),
            56 : Field('total_hemoglobin_conc_max'),
            57 : PercentField('saturated_hemoglobin_percent'),
            58 : PercentField('saturated_hemoglobin_percent_min'),
            59 : PercentField('saturated_hemoglobin_percent_max'),
            62 : Field('device_index'),
            67 : Field('left_pco'),
            68 : Field('right_pco'),
            69 : Field('left_power_phase'),
            70 : Field('left_power_phase_peak'),
            71 : Field('right_power_phase'),
            72 : Field('right_power_phase_peak'),
            73 : SpeedMpsField('enhanced_speed'),
            78 : EnhancedAltitudeField('enhanced_altitude'),
            83 : PercentField('vertical_ratio', 100.0),
            84 : PercentField('stance_time_balance'),
            85 : DistanceMillimetersField('step_length'),
        },
        MessageType.event : {
            0 : EventField('event'),
            1 : EventTypeField(),
            2 : Field('data16'),
            3 : Field('data'),
            4 : Field('event_group'),
            7 : Field('score'),
            8 : Field('opponent_score'),
            9 : Field('front_gear_num'),
            10 : Field('front_gear'),
            11 : Field('rear_gear_num'),
            12 : Field('rear_gear'),
            13 : Field('device_index'),
            15: TimestampField('ts_15'),
        },
        MessageType.source : {},
        MessageType.device_info : {
            0 : Field('device_index'),
            1 : DeviceType(),
            2 : ManufacturerField(),
            3 : Field('serial_number'),
            4 : ProductField(),
            5 : VersionField('software_version'),
            6 : Field('hardware_version'),
            7 : TimeMsField('cum_operating_time', 1000.0),
            10 : BatteryVoltageField('battery_voltage'),
            11 : BatteryStatusField(),
            15 : Field('ant_related'),    # only found on ant devices?
            18 : BodyLocationField('sensor_position'),
            19 : StringField('descriptor'),
            20 : Field('ant_transmission_type'),
            21 : Field('ant_device_number'),
            22 : AntNetworkField(),
            24 : Field('sensor_id'),
            25 : SourceTypeField(),
            27 : StringField('product_name'),
        },
        MessageType.unknown_24 : {
            2 : BytesField('data'),
        },
        MessageType.workout : {
            6 : Field('num_valid_steps'),
            8 : StringField('wkt_name'),
        },
        MessageType.workout_step : {},
        MessageType.schedule : {},
        MessageType.location : {},
        MessageType.weight_scale : {
            0 : WeightField(),
            1 : PercentField('percent_fat'),
            2 : PercentField('percent_hydration'),
            3 : WeightField('visceral_fat_mass'),
            4 : WeightField('bone_mass'),
            5 : WeightField('muscle_mass'),
            7 : Field('basal_met'),
            8 : Field('physique_rating'),
            9 : Field('active_met'),
            10 : Field('metabolic_age'),
            11 : Field('visceral_fat_rating'),
            12 : Field('user_profile_index')
        },
        MessageType.course : {},
        MessageType.course_point : {},
        MessageType.totals : {
            0 : TimeSField('timer_time'),
            1 : DistanceMetersField('distance'),
            2 : CaloriesField('calories'),
            3 : SportField(),
            4 : TimeSField('elapsed_time'),
            5 : Field('sessions'),
            6 : TimeSField('active_time'),
            9 : Field('sport_index'),
        },
        MessageType.activity : {
            0 : TimeMsField('total_timer_time'),
            1 : Field('num_sessions'),
            2 : ActivityField(),
            3 : EventField(),
            4 : EventTypeField(),
            5 : TimestampField('local_timestamp', False),
            6 : Field('event_group'),
        },
        MessageType.software : {
            3 : VersionField('version')
        },
        MessageType.file_capabilities : {},
        MessageType.mesg_capabilities : {},
        MessageType.field_capabilities : {},
        MessageType.file_creator : {
            0 : VersionField('software_version'),
            1 : VersionField('hardware_version'),
            2 : BytesField('data')
        },
        MessageType.blood_pressure : {},
        MessageType.speed_zone : {},
        MessageType.monitoring : {
            0 : Field('device_index'),
            1 : CaloriesField('calories'),
            2 : DistanceCentimetersToMetersField(),
            3 : ActivityBasedCyclesField(),
            4 : TimeMsField('cum_active_time'),
            5 : ActivityTypeField(),
            6 : Field('activity_subtype'),
            7 : Field('activity_level'),
            14 : TemperatureField('temperature_min'),
            14 : TemperatureField('temperature_max'),
            19 : ActiveCaloriesField(),
            24 : ActivityTypeIntensityField('current_activity_type_intensity'),
            26 : TimeSField('timestamp_16'),
            27 : HeartRateField('heart_rate'),
            29 : TimeMinField('duration'),
            31 : DistanceMillimetersToMetersField('ascent'),
            32 : DistanceMillimetersToMetersField('descent'),
            33 : TimeMinField('moderate_activity_time'),
            34 : TimeMinField('vigorous_activity_time'),
            35 : DistanceMillimetersToMetersField('cum_ascent'),
            36 : DistanceMillimetersToMetersField('cum_descent')
        },
        MessageType.training_file : {}, # timestamp, serial_number, creation_time, product_ID, session_style
        MessageType.hrv : {
            0 : TimeMsField('time'),
        },
        MessageType.ant_rx : {},
        MessageType.ant_tx : {},
        MessageType.ant_channel_id : {},
        MessageType.length : {},
        MessageType.monitoring_info : {
            0 : TimestampField('local_timestamp', False),
            1 : ActivityTypeField(),
            3 : CyclesDistanceField(),
            4 : CyclesCaloriesField(),
            5 : CaloriesDayField('resting_metabolic_rate')
        },
        MessageType.battery : {
            0 : TimeMinField('remaining_mins'),
            2 : PercentField('charge')
        },
        MessageType.pad : {},
        MessageType.slave_device : {},
        MessageType.personal_record : {
            0 : PersonalRecordTypeField(),
            1 : SportField(),
            2 : DistanceCentimetersToMetersField('record_distance'),
            3 : DistanceCentimetersToMetersField('record_distance2'),
            4 : DistanceCentimetersToMetersField('actual_distance'),
            5 : PersonalRecordField()
        },
        MessageType.connectivity : {
            0 : BoolField('bluetooth_enabled'),
            1 : BoolField('bluetooth_le_enabled'),
            2 : BoolField('ant_enabled'),
            3 : StringField('name'),
            4 : BoolField('live_tracking_enabled'),
            5 : BoolField('weather_conditions_enabled'),
            6 : BoolField('weather_alerts_enabled'),
            7 : BoolField('auto_activity_upload_enabled'),
            8 : BoolField('course_download_enabled'),
            9 : BoolField('workout_download_enabled'),
            10 : BoolField('gps_ephemeris_download_enabled'),
            11 : BoolField('incident_detection_enabled'),
            12 : BoolField('grouptrack_enabled'),
        },
        MessageType.weather_conditions : {},
        MessageType.weather_alert : {},
        MessageType.cadence_zone : {},
        MessageType.hr : {},
        MessageType.unknown_140 : {
            21 : PosField('position_21'),
            24 : PosField('position_24'),
        },
        MessageType.unknown_141 : {
            1 : TimestampField('ts_1', False),
            2 : TimestampField('ts_2', False),
            4 : PosField('position_4'),
            5 : PosField('position_5'),
        },
        MessageType.segment_lap : {},
        MessageType.memo_glob : {},
        MessageType.sensor : {
            0 : Field('sensor_id'),
            2 : StringField('name'),
            32 : ProductField(),
            33 : ManufacturerField(),
        },
        MessageType.segment_id : {},
        MessageType.segment_leaderboard_entry : {},
        MessageType.segment_point : {},
        MessageType.segment_file : {},
        MessageType.workout_session : {},
        MessageType.watchface_settings : {
            0 : WatchFaceModeField('mode'),
            1 : Field('layout'),
        },
        MessageType.gps_metadata : {},
        MessageType.camera_event : {},
        MessageType.timestamp_correlation : {},
        MessageType.gyroscope_data : {},
        MessageType.accelerometer_data : {},
        MessageType.three_d_sensor_calibration : {},
        MessageType.video_frame : {},
        MessageType.obdii_data : {},
        MessageType.nmea_sentence : {},
        MessageType.aviation_attitude : {},
        MessageType.video : {},
        MessageType.video_title : {},
        MessageType.video_description : {},
        MessageType.video_clip : {},
        MessageType.ohr_settings : {
            0 : SwitchField('enabled'),
        },
        MessageType.exd_screen_configuration : {},
        MessageType.exd_data_field_configuration : {},
        MessageType.exd_data_concept_configuration : {},
        MessageType.field_description : {
            0 : Field('developer_data_index'),
            1 : Field('field_definition_number'),
            2 : FitBaseTypeField('fit_base_type_id'),
            3 : StringField('field_name'),
            4 : Field('array'),
            5 : StringField('components'),
            6 : Field('scale'),
            7 : Field('offset'),
            8 : StringField('units'),
            9 : StringField('bits'),
            10 : StringField('accumulate'),
            13 : FitBaseUnitField('fit_base_unit_id'),
            14 : Field('native_message_num'),
            15 : Field('native_field_num')
        },
        MessageType.dev_data_id : {
            0 : Field('developer_id'),
            1 : BytesField('application_id'),
            2 : ManufacturerField(),
            3 : Field('developer_data_index'),
            4 : Field('application_version')
        },
        MessageType.magnetometer_data : {},
        MessageType.barometer_data : {},
        MessageType.one_d_sensor_calibration : {},
        MessageType.set : {},
        MessageType.stress_level : {
            0 : Field('stress_level_value'),
            1 : TimestampField('stress_level_time', False),
        },
        MessageType.unknown_233 : {
            2 : BytesField('unknown_2'),
        },
        MessageType.local_time : {
            0 : TimestampField('local_timestamp', False)
        },
        MessageType.dive_settings : {},
        MessageType.dive_gas : {},
        MessageType.dive_alarm : {},
        MessageType.exercise_title : {},
        MessageType.dive_summary : {},
        # Names and types for this message are guesses
        MessageType.start : {
            2 : TimestampField('local_timestamp', False),
        },
        # Names and types for this message are guesses
        MessageType.data : {
            0 : BytesField('data'),
        },
        # Names and types for this message are guesses
        MessageType.end : {},
        MessageType.unknown_284 : {
            1 : TimestampField('ts_1', True),
        },
        MessageType.mfg_range_min : {},
        MessageType.mfg_range_max : {},
    }
    reserved_field_indexes = {
        250 : Field('part_index'),
        253 : TimestampField(),
        254 : MessageIndexField('message_index')
    }

    @classmethod
    def get_message_definition(cls, message_type):
        return cls.known_messages.get(message_type, {})
